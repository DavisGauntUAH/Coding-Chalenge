#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages
here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs]

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
                                    'reverse_nodes',
                                    'two_numbers',
                                    'zig_zag'
                                    ]),
    include_package_data=True
    
)