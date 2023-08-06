#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

__VERSION__ = '0.0.12'

assert sys.version_info[0] == 3, "META1-PriceFeed requires Python > 3"

setup(
    name='meta1-pricefeed',
    version=__VERSION__,
    description='Command line tool to assist with price feed generation',
    long_description=open('README.md').read(),
    download_url='https://github.com/meta1-blockchain/meta1-pricefeed/tarball/' + __VERSION__,
    author='Rostislav Gogolauri',
    author_email='rostislav@meta1.io',
    maintainer='Rostislav Gogolauri',
    maintainer_email='rostislav@meta1.io',
    url='http://www.github.com/meta1-blockchain/meta1-pricefeed',
    keywords=['meta1', 'price', 'feed', 'cli'],
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
    ],
    entry_points={
        'console_scripts': [
            'meta1-pricefeed = meta1_pricefeed.cli:main'
        ],
    },
    install_requires=[
        "requests==2.22.0", # Required by graphenlib
        "meta1",
        "uptick",
        "prettytable",
        "click",
        "colorama",
        "tqdm",
        "pyyaml",
        "quandl"
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
)
