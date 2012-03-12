from django.db import models

from djangopypi.models import Package



class PackageIndex(models.Model):
    title = models.CharField(max_length=255)
    url = modles.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_sync = models.DateTimeField(editable=False, null=True, blank=True)
    sparse = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

class PackageSource(models.Model):
    package = models.OneToOneField(Package, related_name='+', unique=True)
    source = models.ForeignKey(PackageIndex, related_name='packages')
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return unicode('%s from %s' % (self.package.name, self.source.title,))

