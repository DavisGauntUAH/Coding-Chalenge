#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='coding-chalenge',
    version='v1.0.0',
    author='Davis Gaunt',
    description='leet code evaluation programs',
    url='https://github.com/DavisGauntUAH/Coding-Chalenge',
    license='Apache 2.0',
    classifiers=[
        'Framework :: Pytest',
        'Topics :: Evaluation',
        'Licesnse :: Freeware',
        'Programing Launguage :: Python :: 3+',
    ],
    packages=find_packages(include=['longest_substring',
                                    'next_permutation',
                                    'reverse_nodes'
                                    ]),
    include_package_data=True
    
)