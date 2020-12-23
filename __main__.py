"""
Roots and Vines Task Manager.

Usage:
  roots-and-vines [options] ...

Options:
  --help -h     Show this help message and exit
  --version -v  Show RaV version number and exit
"""

from sys import argv as sys_argv

from docopt import docopt

from __init__ import __version__
from src.app import App


def main(argv=None):
    args = docopt(__doc__, argv=argv,
                  version=f'Roots and Vines {__version__}')

    App().run()


if __name__ == '__main__':
    main()
