#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.16.0'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='django-teryt-tree',
    version=version,
    description="Django-teryt-tree is a Django app that implements TERYT database as tree by django-mptt.",
    long_description=readme + '\n\n' + history,
    author='Adam Dobrawy',
    author_email='naczelnik@jawnosc.tk',
    url='https://github.com/ad-m/django-teryt-tree',
    packages=[
        'teryt_tree',
    ],
    include_package_data=True,
    install_requires=[
        'django-mptt',
        'django-model-utils',
        'django-autoslug',
        'tqdm'
    ],
    download_url='https://github.com/ad-m/django-teryt-tree/tarball/%s' % (version),
    license="BSD",
    zip_safe=False,
    keywords='django-teryt-tree',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Polish',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)