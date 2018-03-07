#!/usr/bin/env python3

# Author: Fupan Li <fupan.li@windriver.com>
import os
from distutils.core import setup

packages = [
            "wic",
            "wic/plugins/imager",
            "wic/plugins/source",
           ]

setup(name = "wic", 
      scripts=["installer"], 
      version="1.0", 
      description="A installer tool comes from wic", 
      author="Fupan Li", 
      author_email="fupan.li@windriver.com",
      packages=packages
)
