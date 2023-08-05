#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='graphlet_laplacian_counter',
      version='0.21',
      description='Wrapper C++ Graphlet Laplacian Counter',
      author='Sam F. L. Windels',
      author_email='sam.windels@gmail.com',
      # url='https://www.python.org/sigs/distutils-sig/',
      requires=['numpy'], #external packages as dependencies
      packages=['graphlet_laplacian_counter'],
      package_dir={'': 'src'},
      ext_modules = [Extension("_counter",['graphlet_laplacian_counter/c++_src/Counter.cpp'], include_dirs=['src_c++'])]
     )
