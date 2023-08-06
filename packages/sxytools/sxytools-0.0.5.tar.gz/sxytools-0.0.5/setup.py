# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='sxytools',
    packages=find_packages(),
    version="0.0.5",
    description="sxy python script",
    author="shenxiaoyang",
    author_email="380944919@infocore.cn",
    license="GPLv3",
    url='https://github.com/shenxiaoyang/sxytools.git',
    download_url='https://github.com/shenxiaoyang/sxytools.git',
    keywords=['sxytools'],
    classifiers=[],
    zip_safe=False,
    install_requires=[
        'cx_Oracle>=6.2.1',
        'paramiko>=2.4.1'
    ],
    include_package_data=True,
)
