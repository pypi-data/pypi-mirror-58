import setuptools
from distutils.core import setup

setup(
  name = 'pwcnet',
  packages = ['pwcnet'],
  version = '0.2',
  description = 'A pytorch port of PWC-Net',
  author = 'Keunhong Park',
  author_email = 'kpar@cs.washington.edu',
  url = 'https://github.com/keunhong/pytorch-pwc',
  download_url = 'https://github.com/keunhong/pytorch-pwc/archive/0.2.tar.gz',
  keywords = ['python', 'pwcnet'],
  install_requires=['numpy','imageio'],
  classifiers = [],
)

