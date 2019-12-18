from typing import IO
from setuptools import setup, find_packages


def _description() -> str:
    """Returns project description."""
    with open("README.md", "r") as readme:  # type: IO
        return readme.read()


setup(
    name="cli-snakegame",
    version="1.0.0",
    author="Volodymyr Yahello",
    author_email="vyahello@gmail.com",
    description="A simple snake game right in your command line. Just try it, it is fun :)",
    long_description=_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/vyahello/snakegame-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
