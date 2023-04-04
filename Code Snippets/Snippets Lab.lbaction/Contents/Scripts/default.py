#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import os
import re

my_env = os.environ.copy()

items = []

arg = sys.argv[1]
fFiles = sp.check_output('mdfind -onlyin /Users/min/Databases/T000/Script "' + arg + '"', shell=True)
#fFiles = fFiles.splitlines()
fFiles = str(fFiles.decode('utf-8')).split("\n")
if fFiles[0] == "":
    item = {}
    item['title'] = "Found nothing!"
    items.append(item)
else:
    for fFile in fFiles:
        d = sp.check_output('basename `dirname "' + fFile + '"`', shell=True)
        item = {}
        item['title'] = sp.check_output('basename "' + fFile + '"', shell=True).decode("utf-8")
        item['subtitle'] = sp.check_output('cat "' + fFile + '" | sed -e "1d" | tr "\n" "|"', shell=True).decode("utf-8")
        item['action'] = "copy.py"
        item['path'] = fFile
        item['actionArgument'] = fFile
        item['actionRunsInBackground'] = True
        item['icon'] = d.rstrip().decode("utf-8") + "Template.png"
        items.append(item)

print(json.dumps(items))