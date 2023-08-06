# -*- coding: utf-8 -*-
# @Author: durban
# @Date:   2019-12-25 18:00:43
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-26 10:26:14

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Flask-DXCaptcha',
    version='1.0.1',
    url='https://github.com/durban89/flask_dxcaptcha',
    license='MIT',
    author='durban zhang',
    author_email='durban.zhang@gmail.com',
    description='Flask-DXCaptcha是依赖顶象科技提供的无感验证功能开发的Flask 扩展',
    long_description=long_description,
    long_description_content_type="text/markdown",
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
