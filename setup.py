#!/usr/bin/env python
import sys
from setuptools import setup, find_packages
from BioFtParse import __version__

requirements = ["Bio", "pandas", "argparse"]


setup(
    name='BioFtParse',
    author='xu shuangbin',
    author_email='xshuangbin@163.com',
    version=__version__,
    url='http://github.com/xiangpin/',
    description='Multiple Bioinformatics format files parse toolkits',
    license='Apache 2.0',
    packages=find_packages(),
    python_requires='>3.0.0',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
        'parse_genbank.py=BioFtParse.parse_genbank:main'
        ],
    },
    classifiers=[
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
)
