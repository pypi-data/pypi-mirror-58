# vmail-manager
![PyPI - Status](https://img.shields.io/pypi/status/vmail-manager?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/vmail-manager?style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vmail-manager?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/domrim/vmail-manager?style=for-the-badge)

**DISCLAIMER: THIS APPLICATION IS STILL IN ALPHA/BETA STATE. DO NOT USE IT IN PRODUCTIVE ENVIRONMENTS IF YOU DON'T
WHAT YOU'RE DOING!**

`vmail-manager` is a command line to for managing a mail-server database based on the great [HowTo](https://thomas-leister.de/en/mailserver-debian-stretch) ([german version](https://thomas-leister.de/mailserver-debian-stretch/))
from [Thomas Leister](https://thomas-leister.de) written in Python3.

### Features
* manage the tables `domains`, `accounts` and `aliases` (`tlspolicies` support will maybe be added one day)
* supports multiple database backends (if your setup differs from the HowTo, i used postgresql instead of mariadb)

## Installation
### via pip
Install it with `pip3 install vmail-manager`

### manually
Clone this git or download the sources from pypi on your local machine and go into the directory.

_Optional: Create a venv and activate it._

Install all requirements with `pip3 install -r requirements.txt`

Run the tool with `./vmail-manager.py` (or add the folder to your path and create an alias to `vmail-manager`)

## Usage
Use the command help to get started:
```
vmail-manager --help
```

## Configuration
All config values stored in the config file can be overwritten with command line options.

Config files are formatted in [YAML](https://yaml.org/) and loaded via [confuse](https://pypi.org/project/confuse/)
The paths for the config file are (dependent on the OS):

* macOS: ``~/.config/vmail-manager/config.yaml`` and ``~/Library/Application Support/vmail-manager/config.yaml``
* Other Unix (Linux, BSD...): ``$XDG_CONFIG_HOME/vmail-manager/config.yaml`` and ``~/.config/vmail-manager/config.yaml``
* Windows: ``%APPDATA%\vmail-manager\config.yaml`` where the `APPDATA` environment variable falls
  back to ``%HOME%\AppData\Roaming`` if undefined

Some more paths are checked, if you wan't to store your config elsewhere look in the
[confuse documentation](https://confuse.readthedocs.io/en/latest/#search-paths) section about config paths.
