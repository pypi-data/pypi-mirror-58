Snake
-----
An interactive CLI Snake game, tested on Python 2.7 and 3.6 Posix environments.

![Applications list view](https://github.com/jakehadar/py-snake/blob/master/screenshots/screenshot@half.png)

Installation
------------
Install from PyPi using
[pip](http://www.pip-installer.org/en/latest/), a package manager for
Python.

``` {.sourceCode .bash}
 pip install py-snake
```

Or clone the repo and install using setuptools.

``` {.sourceCode .bash}
 cd path/to/repo
 python setup.py develop
```

Usage
-----
Start a new game by running `snake` from from command line. Optionally pass `--help` flag for more info.

``` {.sourceCode .bash}
$ snake --help
usage: snake [-h] [--width WIDTH] [--height HEIGHT] [--speed SPEED]
             [--food FOOD]

Snake game for CLI

optional arguments:
  -h, --help       show this help message and exit
  --width WIDTH    Frame width
  --height HEIGHT  Frame height
  --speed SPEED    Snake speed (fps)
  --food FOOD      Number of food pieces available
```


Uninstallation
--------------
Uninstall Snake completely using pip.

``` {.sourceCode .bash}
 pip uninstall py-snake
```
