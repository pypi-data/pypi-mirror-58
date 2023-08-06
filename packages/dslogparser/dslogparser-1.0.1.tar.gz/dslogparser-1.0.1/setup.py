from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='dslogparser',
      version='1.0.1',
      description='FIRST FRC Driver Station logs parser',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='http://github.com/ligerbots/dslogparser',
      author='Paul Rensing',
      author_email='prensing@ligerbots.org',
      license='MIT',
      download_url='https://github.com/ligerbots/dslogparser/archive/v1.0.1.tar.gz',
      packages=['dslogparser'],
      scripts=['dslog2csv.py'],
      install_requires=[
          'bitstring',
      ],
      zip_safe=False
)
