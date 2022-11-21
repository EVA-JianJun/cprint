#!/usr/bin/env python
# coding: utf-8
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fd:
    long_description = fd.read()

setup(
    name = 'cprint-jianjun',
    version = '1.1.0',
    author = 'jianjun',
    author_email = '910667956@qq.com',
    url = 'https://github.com/EVA-JianJun/cprint',
    description = u'Colorful Print 彩色文本格式化, 彩色文本输出, 控制打印字符颜色样式!',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = ["cprint"],
    install_requires = [
        "forbiddenfruit>=0.1.4",
    ],
    entry_points={
        'console_scripts': [
            'cpshow=cprint:_cpshow',
            'cpshoww=cprint:_cpshoww',
            'cpdemo=cprint:_demo',
        ],
    },
)