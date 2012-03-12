DjangoPyPI Mirroring
====================

DjangoPyPI mirroring is a plugin for the DjangoPyPI application that adds
support for mirroring other repositories. Packages that are hosted by the other
repository will be mirrored when the packages in the repository are mirrored.

You can also choose to selectively mirror packages from another package index so
that only the packages you need are mirrored in your package index.

Installation
------------

Requirements
____________

* djangopypi >= 0.4.4

Path
____

The first step is to get ``djangopypi_mirroring`` into your Python path.

Buildout
++++++++

Simply add ``djangopypii_mirroring`` to your list of ``eggs`` and run buildout 
again.

EasyInstall/Setuptools
++++++++++++++++++++++

If you have setuptools installed, you can use 
``easy_install djangopypi_mirroring``

Manual
++++++

Download and unpack the source then run::

    $ python setup.py install

Django Settings
_______________


If it isn't already there, make sure that ``djangopypi`` is in your 
``INSTALLED_APPS`` list in your Django ``settings.py`` file. Then, add 
``djangopypi_mirroring`` to your ``INSTALLED_APPS`` list as well. Once they are
both added, make sure to run ``manage.py syncdb``.[#]_.

.. [#] ``djangopypi`` and ``djangopypi_mirroring`` are South enabled, if you are 
using South then you will need to run the South ``manage.py migrate`` 
command to get the tables.
