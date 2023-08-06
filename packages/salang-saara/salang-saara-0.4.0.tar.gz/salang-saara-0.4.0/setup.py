#!/usr/bin/env python

from setuptools import setup, find_packages

REQUIRED = [
    "tabulate",
    "simplejson"
]

setup(name='salang-saara',
      version='0.4.0',
      description='A code for transliterating (romanizing) Arabic text using the ALA-LC standard',
      author='CompMusic / MTG UPF',
      url='https://github.com/samlet/saara',
      install_requires=REQUIRED,
      include_package_data=True,
      packages=['aranasyn', 'arramooz', 'asmai', 'collocations', 'collocations.pyarabic', 'mishkal', 'mishkal.tashkeel', 'pyarabic', 'naftawayh', 'tashaphyne', 'qalsadi', 'qalsadi.libqutrub', 'arabic', 'CodernityDB'],

      package_dir={
              'tashaphyne':'tashaphyne',
              'naftawayh':'naftawayh',
              'pyarabic':'pyarabic',
              'qalsadi':'qalsadi',
              'libqutrub':'qalsadi/libqutrub',
              'arabic':'',
              'mishkal':'mishkal'},

      package_data={
              'arramooz': ['data/*'],
              'collocations': ['data/*']}
)
