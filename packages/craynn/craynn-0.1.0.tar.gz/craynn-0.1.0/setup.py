"""
CRAYNN - yet another NN toolkit.
"""

from setuptools import setup, find_packages
import os

here = os.path.dirname(__file__)

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description=f.read()

with open(os.path.join(here, 'VERSION'), encoding='utf-8') as f:
  version=f.read().strip()

setup(
  name = 'craynn',
  version=version,
  description="""Yet another neural network toolkit.""",

  long_description=long_description,
  long_description_content_type="text/markdown",

  url='https://github.com/craynn/craynn',

  author='Maxim Borisyak and contributors.',
  author_email='maximus.been@gmail.com',

  maintainer='Maxim Borisyak',
  maintainer_email='maximus.been@gmail.com',

  license='MIT',

  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],

  packages=find_packages(exclude=['contrib', 'examples', 'docs', 'tests']),

  extras_require={
    'test': [
      'pytest>=4.0.0',
      'scipy>=1.3.0'
    ],
  },

  install_requires=[
    'tensorflow>=2.0.0',
    'numpy>=1.17.1',
    'matplotlib>=3.0.2',
    'pydotplus>=2.0.2',
  ],

  python_requires='>=3.7',
)


