History
=======

0.4.3 (2011-02-22)
------------------

* Moved xmlrpc views into views folder
* Moved xmlrpc command settings to the settings file
* Cleaned up xmlrpc views to remove django.contrib.sites dependency

0.4.2 (2011-02-21)
------------------

* Added CSRF support for Django>=1.2
* Added conditional support to proxy packages not indexed

0.4.1 (2010-06-17)
------------------

* Added conditional support for django-haystack searching

0.4 (2010-06-14)
----------------

* 'list_classifiers' action handler
* Issue #3: decorators imports incompatible with Django 1.0, 1.1
* RSS support for release index, packages
* Distribution uploads (files for releases)

0.3.1 (2010-06-09)
------------------

* Installation bugfix

0.3 (2010-06-09)
----------------

* Added DOAP views of packages and releases
* Splitting djangopypi off of chishop
* Switched most views to using django generic views

Backwards incompatible changes
______________________________

* Refactored package/project model to support multiple owners/maintainers
* Refactored release to match the metadata only that exists on pypi.python.org
* Created a Distribution model for distribution files on a release

0.2.0 (2009-03-22)
------------------

* Registering projects and uploading releases now requires authentication.
* Every project now has an owner, so only the user registering the project can 
  add releases.
* md5sum is now properly listed in the release link.
* Project names can now have dots ('.') in them.
* Fixed a bug where filenames was mangled if the distribution file already existed.
* Releases now list both project name and version, instead of just version in the admin interface.
* Added a sample buildout.cfg. Thanks to Rune Halvorsen (runeh@opera.com).

Backwards incompatible changes
______________________________

* Projects now has an associated owner, so old projects must be exported and 
  imported to a new database.

0.1.0 (2009-03-22)
------------------

* Initial release
