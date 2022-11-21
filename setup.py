#!/usr/bin/env python

from distutils.core import setup

setup(name='answearing_questions',
      version='0.1.0',
      packages=['answering_questions'],
      requires = ["torch", "transormers", "wikipedia"]
     )