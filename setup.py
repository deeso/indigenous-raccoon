#!/usr/bin/env python
from setuptools import setup, find_packages
# import os


# data_files = [(d, [os.path.join(d, f) for f in files])
#               for d, folders, files in os.walk(os.path.join('src', 'config'))]

DESC =''
setup(name='indigenous-raccoon',
      version='1.0',
      description=DESC,
      author='adam pridgen',
      author_email='dso@thecoverofnight.com',
      install_requires=['kombu', 'pymongo', 'toml'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
)
