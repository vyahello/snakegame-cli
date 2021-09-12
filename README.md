![Screenshot](media/logo.png)

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Build Status](https://app.travis-ci.com/vyahello/snakegame-cli.svg?branch=master)](https://app.travis-ci.com/github/vyahello/snakegame-cli)
[![Coverage Status](https://img.shields.io/badge/coverage-56%25-orange)](https://img.shields.io/badge/coverage-56%25-orange)
[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![License: GPL-3.0](https://img.shields.io/github/license/vyahello/snakegame-cli)](LICENSE.md)
[![PyPI version shields.io](https://img.shields.io/pypi/v/cli-snakegame.svg)](https://pypi.python.org/pypi/cli-snakegame/)
[![PyPi downloads](https://img.shields.io/pypi/dm/cli-snakegame.svg)](https://pypi.python.org/pypi/cli-snakegame)
[![Downloads](https://pepy.tech/badge/cli-snakegame)](https://pepy.tech/project/cli-snakegame)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/cli-snakegame.svg)](https://pypi.python.org/pypi/cli-snakegame/)

# Terminal snake game
> A simple snake game right in your terminal using python built-in **curses** package.

## Tools/features

### Production

- python 3.4, 3.5, 3.6, 3.7, 3.8
- [curses](https://docs.python.org/3/library/curses.html)
- OS compatibility
  - Linux
  - Mac

### Development

- [travis CI](https://travis-ci.org/)
- [pytest](https://pypi.org/project/pytest/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [black](https://black.readthedocs.io/en/stable/)
- [pylint](https://www.pylint.org/)
- [flake8](http://flake8.pycqa.org/en/latest/)

## Usage
Please press **esc** or **cntl+c** to stop the game.

![Demo](media/usage.gif)

### Installation
Please run following script to obtain latest package from PYPI:
```bash
pip install cli-snakegame
```
Please execute `pysnake` CLI tool from your shell:
```bash
pysnake
```

### Run from source code

Please execute command from the root of your source directory:
```bash
python -m snake
```

## Development notes

### Run code analysis
In general static code analysis consists of following tools: `black`, `flake8`, `pylint`, `mypy` and `unittests` accordingly.
To be able to start static code analysis **locally** please run following script from the root directory of the project:
```bash
./analyse-code.sh install-dependencies
```
Anyway, this script is triggered via `Travis CI`.

### Run unittests
Also you can run unittests separately. Please run script from the root directory of the project:
```bash
pytest
```
After please open `test-report.html` file to see detailed testing report

### Release notes

Please refer to [CHANGELOG](CHANGELOG.md) file to get more details

### Meta
Author – Volodymyr Yahello (vyahello@gmail.com).

Distributed under the `GNU` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all project development dependencies
