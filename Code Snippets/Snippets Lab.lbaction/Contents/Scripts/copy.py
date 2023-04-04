#!/usr/local/bin/python3

import sys
import subprocess as sp
import os
import ast

my_env = os.environ.copy()
actionArgument = sys.argv[1]
sp.check_output("cat '" + actionArgument + "'| sed -e '1d' -e '$d' | pbcopy", shell=True)
os.system('afplay /System/Library/Sounds/Purr.aiff')