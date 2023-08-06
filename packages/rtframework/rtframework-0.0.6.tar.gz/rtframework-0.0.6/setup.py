from setuptools import setup, find_packages

setup(name="rtframework", packages=find_packages())

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="rtframework",
    version="0.0.6",
    author="Alex Makasoff",
    author_email="alexmakasoff@gmail.com",
    description="Test framework geared for stress and load testing",
    long_description=long_description,
    # long_description_content_type="text/restructuredtext",
    url="https://github.com/Roba-Boba/rtframework",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)