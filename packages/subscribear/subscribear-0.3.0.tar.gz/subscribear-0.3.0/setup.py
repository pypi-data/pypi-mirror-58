import io
import os
import re

from setuptools import setup, find_packages

__version__ = '0.3.0'


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name='subscribear',
    version=__version__,
    author='nicuzs',
    license=read('LICENSE'),
    author_email='support@nicuzs.tech',
    url='https://test.pypi.org/project/subscribear/',
    description='Will explain later ... ',
    long_description=read('README.md'),
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'boto3>=1.10.37'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython'
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.7',
)
