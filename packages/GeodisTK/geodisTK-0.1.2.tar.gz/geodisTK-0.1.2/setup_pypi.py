# -*- coding: utf-8 -*-
import setuptools 

# Get the summary
description = 'An open-source toolkit to calculate geodesic distance' + \
              ' for 2D and 3D images'

# Get the long description
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name    = 'geodisTK',
    version = "0.1.1",
    author  ='Guotai Wang',
    author_email = 'wguotai@gmail.com',
    description  = description,
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url      = 'https://github.com/taigw/geodesic_distance',
    license  = 'MIT',
    packages = setuptools.find_packages('cpp'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    python_requires = '>=3.6',
)
