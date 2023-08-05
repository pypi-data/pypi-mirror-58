#! /usr/bin/python3

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='cobblestone',
      version='0.2',
      description='Cobblestone: Basic game engine',
      author='Marco Meyer',
      author_email='marco.meyerconde@gmail.com',
      long_description_content_type="text/markdown",
      long_description=long_description,
      license='MIT',
      packages=['cobblestone'],
      zip_safe=False)

	#      url='http://github.com/storborg/funniest',

