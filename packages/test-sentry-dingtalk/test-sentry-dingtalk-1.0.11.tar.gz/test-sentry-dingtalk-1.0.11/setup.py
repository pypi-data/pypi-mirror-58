#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sentry-Dingtalk
==============

An extension for Sentry which integrates with Dingtalk. It will send
notifications to dingtalk robot.

:copyright: (c) 2017 by guoyong yi, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages

# See http://stackoverflow.com/questions/9352656/python-assertionerror-when-running-nose-tests-with-coverage
# for why we need to do this.
from multiprocessing import util


tests_require = [
]

install_requires = [
    'sentry>=9.1.0',
]


setup(
    name='test-sentry-dingtalk',
    version='1.0.11',
    keywords='test-sentry-dingtalk',
    author='dazao',
    author_email='zhaodazao@gmail.com',
    url='https://code.aliyun.com/PlayGoods-Materiel/wanwu-senstry-dingtalk.git',
    description='A Sentry extension which integrates with Dingtalk robot. test',
    long_description=__doc__,
    long_description_content_type='text/markdown',
    license='BSD',
    platforms='any',
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='nose.collector',
    entry_points={
        'sentry.plugins': [
            'dingtalk = sentry_dingtalk.plugin:DingtalkPlugin'
        ],
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

