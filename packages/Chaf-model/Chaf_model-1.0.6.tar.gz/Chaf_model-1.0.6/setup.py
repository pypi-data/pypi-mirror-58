#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: chaf
# Mail: chaf@mail.ustc.deu.cn
# Created Time:  2019-12-13 20:59:00
#############################################

from setuptools import setup, find_packages            #这个包没有的可以pip一下

setup(
    name = "Chaf_model",      #这里是pip项目发布的名称
    version = "1.0.6",  #版本号，数值大的会优先被pip
    keywords = ("pip", "Chaf_model","featureextraction"),
    description = "An feature extraction algorithm",
    long_description = "An feature extraction algorithm, improve the FastICA",
    license = "MIT Licence",

    url = "https://github.com/Chaphlagical",     #项目相关文件地址，一般是github
    author = "WenboChen",
    author_email = "chaf@ustc.edu.cn",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    #install_requires = ["numpy"]          #这个项目需要的第三方库
)