#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
            join(dirname(__file__), *names),
            encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='pygaps',
    version='2.0.2',
    license='MIT license',
    description='A framework for processing adsorption data for porous materials',
    long_description='%s' % (
        re.compile('^.. start-badges.*^.. end-badges',
                   re.M | re.S).sub('', read('README.rst'))
    ),
    author='Paul Iacomi',
    author_email='iacomi.paul@gmail.com',
    url='https://github.com/pauliacomi/pygaps',
    project_urls={
        "Documentation": 'https://pygaps.readthedocs.io',
        "Source Code": 'https://github.com/pauliacomi/pygaps',
    },
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: PyPy3',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    keywords=[
        'adsorption', 'characterization', 'porous materials'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    install_requires=[
        'numpy >= 1.13',
        'scipy >= 1.0.0',
        'pandas >= 0.21.1',
        'matplotlib >= 2.1',
        'xlrd >= 1.1',
        'xlwt >= 1.3',
        'coolprop >= 6.0',
        'requests',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'coverage',
        'nose',
    ],
    extras_require={
        'dev': [
            'isort',
            'pylint',
            'flake8',
            'autopep8',
            'pydocstyle',
            'bump2version',
        ],
        'docs': [
            'docutils >= 0.11'
            'doc8',
            'pandoc',
            'restructuredtext-lint',
            'sphinx',
            'nbsphinx',
            'sphinx_rtd_theme',
        ],
    },
)
