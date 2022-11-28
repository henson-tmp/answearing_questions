#!/usr/bin/env python

from distutils.core import setup

from question_answering.version import __version__ as package_version

setup(name='question_answering',
      version=package_version,
      packages=['question_answering'],
      install_requires = [
            "spacy",
            "torch", 
            "transformers", 
            "wikipedia"
      ],
      entry_points={
            "console_scripts": ["qa = question_answering.__main__:main"]
      },
     )