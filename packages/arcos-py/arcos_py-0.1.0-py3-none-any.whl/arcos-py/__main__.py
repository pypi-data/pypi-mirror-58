# Main (Raw) Functions

from configparser import ConfigParser
from importlib import resources  # Python 3.7+
import sys

from arcos-py import raw
from arcos-py import supplemental
from arcos-py import summary
from arcos-py import national


if __name__ == "__main__":
    main()