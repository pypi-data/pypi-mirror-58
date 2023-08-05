# wynn.py

[![Documentation Status](https://readthedocs.org/projects/wynnpy/badge/?version=latest)](https://wynnpy.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/wynn.py)](https://pypi.org/project/wynn.py/)

A Python wrapper for the Wynncraft public API

## Basic usage

API wrappers are found under the `wynn` package. To fetch a player's
data, for example, you can use

```python
wynn.player.get_player('playerName')
```
