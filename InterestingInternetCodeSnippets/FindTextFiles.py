'''
Copied from:
http://hundredminutehack.blogspot.com/2016/02/processing-lots-of-text-files-with.html

Prefix for UNC raw quotes: r'\\uncpath\dir\dir'
'''
import os
from collections import Counter


def pyfiles():
    base_dir = "/Users/UserName/Directory"
    for dir_name, child_dirs, files in os.walk(base_dir):
        for file_name in files:
            if file_name.endswith(".py"):
                full_path = "{}{}{}".format(dir_name, os.path.sep, file_name)
                yield full_path


def pick_lines(file_name):
    with open(file_name, "rt", encoding="utf-8") as fileob:
        for line in fileob:
            if line.strip().startswith("bl_region_type"):
                yield line


for pyfile in pyfiles():
    print(pyfile)


region_types = []
for pyfile in pyfiles():
    for line in pick_lines(pyfile):
        _, region_type = line.split("=")
        region_type = region_type.replace("'", "")
        region_type = region_type.replace("\"", "")
        region_type = region_type.strip()

        region_types.append(region_type)


counts = Counter(sorted(region_types))
for key, val in counts.items():
    print("{}: {}".format(key, val))
    
