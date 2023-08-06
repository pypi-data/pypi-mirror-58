import setuptools
from codecs import open


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="koe-acoustic-features",
    version="0.0.2",
    author="Yukio Fukuzawa",
    author_email="y.fukuzawa@massey.ac.nz",
    description="Implementation of acoustic features used by Koe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fzyukio/koe-acoustic-features",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'scipy'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)