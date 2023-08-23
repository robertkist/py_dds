"""
Run to perform an in-place installation:
    > pip install --editable .
To build a .whl, run:
    > python3 setup.py bdist_wheel
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='py_dds',  # package name
    version='0.9',
    packages=['py_dds'],
    package_dir={'': 'src'},
    author="Robert Kist",
    author_email="rk@robertkist.com",
    description="A loader for .DDS files for Python 3.9 and newer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robertkist/py_dds",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
