# -*- coding: utf-8 -*-
"""
Requirements:
1. Script in directory with CSV files.
2. Text file named "DeleteThese.txt" containing names to exclude.

Actions:
1. Creates a list of every CSV file in current directory.
2. Creates a list of names to be excluded.
3. Creates a copy of each original CSV, adding the "Legal_" prefix.
4. Copies only lines that do not contain names in "DeleteThese.txt"
"""
import glob

files = [f for f in glob.glob("*.csv")]

datanames = open('DeleteThese.txt').read().splitlines()

for f in files:
    with open(f) as oldfile, open('Legal_' + f, 'w') as newfile:
        for line in oldfile:
            if not any (datanames in line for datanames in datanames):
                newfile.write(line)