import os
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
  long_description = fh.read()

setup(
  name='getserv',
  version=os.getenv('PACKAGE_VERSION', '0.0.0'),
  author='Davide Perozzi',
  author_email='myself@davideperozzi.com',
  description='Retrieve a stable server to deploy',
  entry_points={
    'console_scripts': [
      'getserv=getserv.__main__:main'
    ]
  },
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/davideperozzi/getserv',
  packages=find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
)
