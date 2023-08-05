
# coding=utf-8

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aep-python-sdk-v3",
    version="1.1.3",
    author="Enzo Liang",
    author_email="liangyzh@inspur.com",
    description="aep sdk tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://apicloud.inspur.com/",
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "Operating System :: OS Independent",
                 ],
    keywords=['sdk', 'tool'],
    install_requires=['requests>=2.14.2'],
    python_requires='>=3'
)
