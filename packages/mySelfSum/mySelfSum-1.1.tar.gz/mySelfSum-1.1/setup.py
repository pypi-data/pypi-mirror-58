#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/28 15:09
# @Author  : ZhangYuge
# @File    : setup.py.py

from setuptools import setup

setup(
    name='mySelfSum',# 需要打包的名字,即本模块要发布的名字
    version='v1.1',#版本
    description='A  module for test', # 简要描述
    py_modules=['mySelfSum'],   #  需要打包的模块
    author='Squidward', # 作者名
    author_email='vzhyu@foxmail.com',   # 作者邮件
    url='https://github.com/vfrtgb158/email', # 项目地址,一般是代码托管的网站
    # requires=['requests','urllib3'], # 依赖包,如果没有,可以不要
    license='MIT'
)
