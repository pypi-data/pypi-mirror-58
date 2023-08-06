#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 14:46
# @Author  : ZhangYuge
# @File    : setup.py.py


# from distutils.core import setup
from setuptools import setup
# setup(name='printtest',
#       version='1.0',
#       py_modules=['printtest'],
#       )

# with open("README.txt", "r",encoding='utf-8') as fh:
#     long_description = fh.read()

setup(
    name='py3_email',#需要打包的名字
    version='v1.0',#版本
    description='A very simple module for send email',
    py_modules=['py3_email'],#需要打包的模块
    author='Squidward',
    author_email='vzhyu@foxmail.com',
    requires=['smtplib','email'],
    url='https://github.com/vfrtgb158/email',
    license='MIT',
)

# setup(
#     name='pymail',
#     version='1.0.0',
#     description='A very simple packet for send email',
#     author='Squidward',
#     author_email='vzhyu@foxmail.com',
#     url='https://github.com/vfrtgb158/email',
#     license='MIT',
#     keywords=['email','mail'],
#     project_urls={
#     'Documentation': 'https://github.com/vfrtgb158/email'
#
#     },
#     # packages=['pymail'],
#     # install_requires=['numpy>=1.14', 'tensorflow>=1.7'],
#     python_requires='>=3'
#     )


# setup(
#     name="pymail",
#     version="1.0",
#     author="Squidward",
#     author_email="vzhyu@foxmail.com",
#     description='A very simple packet for send email',
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/vfrtgb158/email",
#     py_modules=['pymail'],#需要打包的模块
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     python_requires='>=3',
# )


