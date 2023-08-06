import setuptools
from setuptools import find_packages


setuptools.setup(
    name = 'ByHelpers',
    packages = ['ByHelpers'], # this must be the same as the name above
    version = '0.1.6',
    description = 'Library used by ByPrice scrapers',
    author = 'Kevin B. Garcia Alonso',
    author_email = 'kevangy@hotmail.com',
    url = 'https://github.com/ByPrice/ByHelpers', # use the URL to the github repo
    download_url = 'https://github.com/ByPrice/ByHelpers/',
    keywords = ['ByPrice'],
    install_requires=[
        'pika==0.11.0',
        'fuzzywuzzy==0.16.0',
        'google-cloud-logging==1.10.0'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)
