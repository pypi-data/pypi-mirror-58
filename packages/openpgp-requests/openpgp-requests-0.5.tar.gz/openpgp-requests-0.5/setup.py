from setuptools import setup

# Imports content of requirements.txt into setuptools' install_requires
with open('requirements.txt') as f:
      requirements = f.read().splitlines()

# Imports content of README.md into setuptools' long_description
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
      long_description = f.read()

# sets setup up :P
setup(name='openpgp-requests',
      version='0.5',
      description='A wrapper to the requests module adding OpenPGP support.',
      url='https://github.com/buanzo/openpgp-requests',
      author='Arturo "Buanzo" Busleiman',
      author_email='buanzo@buanzo.com.ar',
      packages=['openpgp_requests'],
      python_requires='>=3.6',
      install_requires=requirements,
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)
