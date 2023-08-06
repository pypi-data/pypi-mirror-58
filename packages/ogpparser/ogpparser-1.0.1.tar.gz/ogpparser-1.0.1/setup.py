from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ogpparser',
    packages=find_packages(),

    version='1.0.1',

    license='MIT',

    install_requires=['beautifulsoup4'],

    author='reeve0930',
    author_email='reeve0930@gmail.com',

    url='https://github.com/reeve0930/ogpparser',

    description='Open Graph Protocolのタグを取得',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='OGP OpenGraphProtocol parser', 

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
    ],
)
