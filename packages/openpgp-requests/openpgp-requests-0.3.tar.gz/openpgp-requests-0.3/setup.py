from setuptools import setup

with open('requirements.txt') as f:
      requirements = f.read().splitlines()

setup(name='openpgp-requests',
      version='0.3',
      install_requires=requirements,
      description='A wrapper to the requests module adding OpenPGP support.',
      url='https://github.com/buanzo/python-http-openpgp-api-tools/tree/master/python-requests-openpgp-api',
      author='Buanzo',
      author_email='buanzo@buanzo.com.ar',
      packages=['openpgp_requests'],
      python_requires='>=3.6',
      zip_safe=False)
