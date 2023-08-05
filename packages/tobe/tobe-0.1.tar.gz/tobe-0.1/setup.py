#-*- encoding: UTF-8 -*-
import setuptools
import tobe

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "tobe",
    #version = tobe.__version__,
    version = '0.1',
    author="hiyang",
    author_email="echohiyang@foxmail.com",
    description="A small ssh list tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PoplarYang",
    packages = ["tobe"],
    #packages=setuptools.find_packages(),
    install_requires = [
        "colorama>=0.4.1"
    ],
    entry_points={
        'console_scripts': [
            'tobe=tobe:run'
        ],
    },
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
