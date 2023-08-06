# -*- coding: utf-8 -*-
# @Author: durban
# @Date:   2019-12-25 18:00:43
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-25 19:03:55

from setuptools import find_packages, setup


setup(
    name='Flask-DXCaptcha',
    version='1.0.0',
    url='https://github.com/durban89/flask_dxcaptcha',
    license='BSD',
    author='durban zhang',
    author_email='durban.zhang@gmail.com',
    description='Flask-DXCaptcha是依赖顶象科技提供的无感验证功能开发的Flask 扩展',
    long_description=__doc__,
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
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
