""" import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1]) """

import sys

from saying import hello


if len(sys.argv) == 2:
    hello(sys.argv[1])
