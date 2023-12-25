#!/usr/bin/env python

#from distutils.core import setup

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
import re
import os

PKG = 'oauthclient'

version = __import__(PKG).get_version()

long_desc = """eBay OAuth client library is a simple 
and easy-to-use library for integrating with eBay 
OAuth and designed to be used for OAuth 2.0 specification 
supported by eBay. There are multiple standard clients that 
can be used with eBay OAuth, such as Spring OAuth client. 
However, this library in addition to functioning as a simple 
eBay OAuth client, helps with additional features such as 
cached App tokens. There are also future enhancements planned 
to add id_token support, 'login with eBay' support etc """

setup(
    name=PKG,
    version=version,
    description="eBay OAuth Client Library",
    author="Anthony Nguyen",
    author_email="hungdao1152002@gmail.com",
    url="https://github.com/Anthony-D11/ebay-oauth-python-client",
    license="COMMON DEVELOPMENT AND DISTRIBUTION LICENSE (CDDL) Version 1.0",
    packages=find_packages(include=['oauthclient', 'oauthclient.*']),
    provides=[PKG],
    install_requires=['lxml', 'requests'],
    test_suite='test',
    long_description=long_desc,
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)