# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 20:24:52 2017

@author: mikew
"""

import glob
import re

fileList = glob.glob('./*.txt')

fullMatch = []

for file in fileList:
    with open(file,'r') as current:
        text = "".join(current.read().split())
        match = re.findall(r'thisisa[\d][\d]{5}teststring',text)
        if len(match) > 0:
            for string in match:
                print(string)
                print(string[8:13])
                fullMatch.append(string[8:13])

print(fullMatch)