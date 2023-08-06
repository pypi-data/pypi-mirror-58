# Emgen 📧
[![Versioning: CalVer](https://img.shields.io/badge/calver-YYYY.MM.DD.MICRO-22bfda.svg)](https://calver.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/github/license/etedor/emgen.svg)](https://github.com/etedor/emgen/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/emgen.svg)](https://pypi.org/project/emgen/)

**Emgen** generates random email addresses.

[![asciicast](https://etedor.github.io/emgen/README-demo.gif)](https://asciinema.org/a/Fk03dQR4GaQhOElBjl8VS8Qz6)

## Installation
Emgen is available on [PyPI](https://pypi.org/project/emgen/) and is installable with [pip](https://pip.pypa.io/en/stable/installing/):
```
$ pip3 install --user emgen
```

## Usage
```
$ emgen --help
usage: emgen [-h] [-c] [-d DOMAIN] [-l LENGTH] [-v]

Generate random email addresses.

optional arguments:
  -h, --help            show this help message and exit
  -c, --clipboard       copy addr to clipboard (default: False)
  -d DOMAIN, --domain DOMAIN
                        set the addr domain portion (default: example.com)
  -l LENGTH, --length LENGTH
                        length of the local-part (from 1 to 64) (default: 8)
  -v, --version         show program's version number and exit
```

Generate an email address for your domain `corgi.example`:
```
$ emgen --domain corgi.example
aiemil8u@corgi.example
```

Generate a long email address for your domain `dane.example`:
```
$ emgen --domain dane.example --length 16
vqjo0h8y4z2dgetd@dane.example
```

Make an alias to generate an address and copy it to your clipboard:
```
$ alias em="emgen -d greyhound.example -l12 --clipboard"
$ em
yx4su4olx2uq@greyhound.example
$ # display the contents of your clipboard:
$ xclip -sel clip -o
yx4su4olx2uq@greyhound.example
```

## License

Emgen is released under the [MIT License](https://opensource.org/licenses/MIT).
