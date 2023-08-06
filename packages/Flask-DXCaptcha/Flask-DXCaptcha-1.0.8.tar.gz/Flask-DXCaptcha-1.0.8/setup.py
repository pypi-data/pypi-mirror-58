# -*- coding: utf-8 -*-
# @Author: durban
# @Date:   2019-12-25 18:00:43
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-27 10:46:15

import io
from setuptools import find_packages, setup

with io.open("README.rst", "rt", encoding='utf8') as f:
    readme = f.read()

setup(
    name='Flask-DXCaptcha',
    version='1.0.8',
    url='https://github.com/durban89/flask_dxcaptcha',
    license='MIT',
    author='durban zhang',
    author_email='durban.zhang@gmail.com',
    description='Flask-DXCaptcha是依赖顶象科技提供的无感验证功能开发的Flask 扩展',
    long_description=readme,
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=1.1.1'
    ],
    python_requires=">=3.7.4",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
