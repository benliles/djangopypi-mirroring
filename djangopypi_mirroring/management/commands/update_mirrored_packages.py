"""

"""

from datetime import datetime
import urllib
import os.path
from time import mktime
from xmlrpclib import ServerProxy

from django.core.files import File
from django.core.management.base import BaseCommand
from djangopypi.models import *



class Command(BaseCommand):
    help = """Load all classifiers from pypi. If any arguments are given,
they will be used as paths or urls for classifiers instead of using the
official pypi list url"""

    def handle(self, *args, **options):
        for index in MasterIndex.objects.all():
            rpc = ServerProxy(index.url)
            try:
                last = index.logs.latest()
            except:
                print 'Error getting latest update for %s' % (str(index),)
                continue
            
            newer = MirrorLog.objects.create(master=index, created=datetime.now())
            
            print 'Looking at changes since: %d' % (mktime(last.created.timetuple()),)
            for update in rpc.changelog(int(mktime(last.created.timetuple()))):
                print str(update)
                package, created = Package.objects.get_or_create(name=update[0])
                
                if update[3] == 'new release':
                    release, created = Release.objects.get_or_create(
                        package=package, version=update[1])
                    
                    if created:
                        newer.releases_added.add(release)
                    
                    pkg_data = rpc.release_data(update[0],update[1])
                    print 'Retrieved release data: %s' % (str(pkg_data),)
                    if 'name' in pkg_data:
                        del pkg_data['name']
                    if 'version' in pkg_data:
                        del pkg_data['version']
                    
                    for key, value in pkg_data.iteritems():
                        if key != 'classifier':
                            release.package_info[key] = value
                        else:
                            release.package_info.setlist(key, value)
                    
                    release.save()
                elif update[3] == 'remove':
                    Release.objects.filter(package=package, version=update[1]).delete()
                elif update[3].startswith('add source file'):
                    try:
                        release = Release.objects.get(package=package,
                                                      version=update[1])
                    except Release.DoesNotExist:
                        continue
                    downloads = rpc.release_urls(update[0], update[1])
                    for download in downloads:
                        print 'Download data: %s' % (str(download),)
                        dist, created = Distribution.objects.get_or_create(release=release,
                            filetype=download['packagetype'],
                            pyversion=download['python_version'])
                        
                        if not created and dist.md5_digest != download['md5_digest']:
                            dist.md5_digest = download['md5_digest']
                            dist.content = File(urllib.urlopen(download['url']))
                        
                        dist.comment = download['comment_text']
                        
                        dist.save()
                
        
