# -*- coding: utf-8 -*-
from pathlib import Path
from setuptools import find_packages
from setuptools import setup

from procrust import __name__, __version__, __description__


setup(
    name=__name__,
    version=__version__,
    url='https://github.com/yaph/procrust',
    license='MIT',

    author='Ramiro Gómez',
    author_email='code@ramiro.org',

    description=__description__,

    entry_points={
        'console_scripts': [
            'procrust=procrust.procrust:main',
        ],
    },

    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',

    packages=find_packages(exclude=('tests',)),

    install_requires=['python-hosts'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
