#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: LiangjunFeng
# Mail: zhumavip@163.com
# Created Time:  2018-4-16 19:17:34
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "ustccomplex",      #这里是pip项目发布的名称
    version = "0.2.0",  #版本号，数值大的会优先被pip
    keywords = ("pip", "ustccomplex","complex"),
    description = "A complex network toolbox",
    long_description = "A complex network toolbox, especially for cnns",
    license = "MIT Licence",

    url = ""  ,#项目相关文件地址，一般是github
    author = "qstan",
    author_email = "tqs@mail.ustc.edu.cn",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["torch"]          #这个项目需要的第三方库
)

