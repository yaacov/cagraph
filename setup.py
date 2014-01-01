#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(name='cagraph',
      version='1.2',
      description='Simple chart class using pygtk and cairo',
      author='Yaacov Zamir',
      author_email='kobi.zamir@gmail.com',
      url='http://code.google.com/p/cagraph',
      packages=['cagraph', 'cagraph/axis', 'cagraph/series']
     )
     
