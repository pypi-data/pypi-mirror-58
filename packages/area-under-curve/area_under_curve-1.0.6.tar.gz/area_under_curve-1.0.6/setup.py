#!/usr/bin/env python
"""package setup"""
import sys
from setuptools import setup

if sys.version_info < (3, 7):
    sys.exit('Sorry, Python < 3.7 is not supported')



setup(name='area_under_curve',
      version='1.0.6',
      description='Calculate area under curve',
      long_description=open('README.rst').read(),
      url='https://github.com/smycynek/area_under_curve',
      author='Steven Mycynek',
      author_email='sv@stevenvictor.net',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'
      ],

      packages=['area_under_curve'],
      keywords='riemann-sum calculus',
      zip_safe=False)
