#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages
    
import os

setup(
    name = "django-piston",
    version = "0.2.3rc2-CORE",
    url = 'https://github.com/timecore/django-piston',
	download_url = 'http://pypi.globoi.com/django-piston/',
    license = 'BSD',
    description = "Piston is a Django mini-framework creating APIs.",
    author = 'Jesper Noehr',
    author_email = 'jesper@noehr.org',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
