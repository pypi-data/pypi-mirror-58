# -*- coding: utf-8 -*-
from setuptools import setup
# from distutils.core import setup

setup(
    name='ege_utils',
    description='Utils classes for EGE project',
    long_description='Utils classes for EGE project',
    license='MIT',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    packages=['ege_utils', 'ege_utils/templates'],
    include_package_data=True,
    version='1.4.0',
    download_url='https://github.com/CoticEaDIFRN/ege_utils/releases/tag/1.4.0',
    url='https://github.com/CoticEaDIFRN/ege_utils',
    keywords=['EGE', 'JWT', 'Django', 'Auth', 'SSO', 'client', ],
    install_requires=['PyJWT==1.7.1', 'requests==2.21.0', 'django>=2.0'],
    classifiers=[]
)
