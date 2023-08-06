from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="zqpy",
    version="0.1.1",
    author="ZhouQing",
    author_email="1620829248@qq.com",
    description="Python Base File",
    license="MIT",
    url="",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
            #'pandas>=0.20.0',
            #'numpy>=1.14.0'
    ],
    zip_safe=True,
)