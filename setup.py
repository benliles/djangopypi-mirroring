import os
from setuptools import setup, find_packages

def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = '0.1'

setup(
    name='djangopypi-mirroring',
    version=version,
    description="A plugin for the Django PyPI for mirroring other package " \
            "repositories",
    long_description=fread("README.rst")+"\n\n" + fread('Changelog.rst') + \
            "\n\n" + fread('AUTHORS.rst'),
    classifiers=[
        "Framework :: Django",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Topic :: System :: Software Distribution",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='django pypi packaging index',
    author='Benjamin Liles',
    author_email='benliles@gmail.com',
    maintainer='Benjamin Liles',
    maintainer_email='benliles@gmail.com',
    url='http://github.com/benliles/djangopypi_mirroring',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'docutils',
        'djangopypi>=0.4.4'
    ],
)
