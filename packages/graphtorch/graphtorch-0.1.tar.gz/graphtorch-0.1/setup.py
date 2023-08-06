from setuptools import setup, find_packages


setup(
    name             = 'graphtorch',
    version          = '0.1',
    description      = 'Package converts sparse graph to matrix',
    long_description = open('README.md').read(),
    author           = 'Hyeonwoo Yoo',
    author_email     = 'hyeon95y@gmail.com',
    url              = 'https://github.com/KU-BIG/graphtorch',
    download_url     = 'https://github.com/KU-BIG/graphtorch',
    packages         = find_packages(),
    classifiers      = [
        'Programming Language :: Python :: 3.6'
    ]
)