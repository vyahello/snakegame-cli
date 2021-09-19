from typing import IO, Sequence
from setuptools import setup, find_packages


def __description() -> str:
    """Returns project description."""
    with open("README.md", "r") as readme:  # type: IO
        return readme.read()


def __requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    with open("requirements.txt", "r") as requirements:  # type: IO
        return tuple(map(str.strip, requirements.readlines()))


if __name__ == "__main__":
    setup(
        name="cli-snakegame",
        version="1.3.0",
        author="Volodymyr Yahello",
        author_email="vyahello@gmail.com",
        description="A simple snake game right in your command line. "
        "Just try it, it is fun :)",
        long_description=__description(),
        long_description_content_type="text/markdown",
        url="https://github.com/vyahello/snakegame-cli",
        packages=find_packages(),
        include_package_data=True,
        install_requires=__requirements(),
        classifiers=[
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS",
        ],
        python_requires=">=3.4",
        entry_points={"console_scripts": ["pysnake = snake.__main__:main"]},
    )
