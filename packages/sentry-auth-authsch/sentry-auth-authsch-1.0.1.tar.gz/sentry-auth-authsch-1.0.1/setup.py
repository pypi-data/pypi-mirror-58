#!/usr/bin/env python
"""
sentry-auth-authsch
============

A Sentry integration which enables `AuthSCH <https://auth.sch.bme.hu/>`_  authentication.

:copyright: (c) 2019 by Tamas Kiss
:license: Simplified BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


install_requires = [
    'requests>=2.20,<3.0.0'
]

tests_require = [
    'exam',
    'responses',
    'flake8>=2.0,<2.1',
    'pytest<3.6.0,>=3.5.0',
    'betamax==0.8.1',
    'sentry>=9.1.0,<10.0.0',
]

setup(
    name='sentry-auth-authsch',
    version='1.0.1',
    author='Tamas Kiss',
    author_email='tamas.kiss@kszk.bme.hu',
    url='https://github.com/thomasklein94/sentry-auth-authsch.git',
    description='AuthSCH SSO integration for Sentry',
    long_description=open('README.rst').read(),
    license='Simplified BSD',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
    },
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'sentry_auth_authsch = sentry_auth_authsch',
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
