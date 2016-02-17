# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:44:17 2016

@author: mikew
"""

import pandas as pd
import xml.etree.ElementTree as ET

"""
print('=====================XML=====================')
tree = ET.parse('test.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    print(child[-1].text)
"""


"""
print('=====================CSV-READLINES=====================')   

x = open('testcsv.csv', 'r').readlines()
y = x[0]
z = x[1:len(x)]

columns = {'DOCID': 1}

for i in z:
    docid = i.split(',')[0]
    rest = i[len(docid)+2:-2]
    delilist = []
    parsed = ET.fromstring(rest)
    for child in parsed:
        delilist.append(child[-1].text)
    print(list(columns.keys()))
    print(docid, ',', ' '.join(delilist))
"""
    
print('=====================CSV-DATAFRAME=====================')

"""
To do:
1. Create separate DAT overlay files for each field (DOCID + field)
2. Check for a document with multiple updates to the same field, only keep
    latest value.
"""

# Reads CSV into memory as a dataframe, beware quotechar/CSV defaults
df = pd.read_csv('testcsv.csv', quotechar='^')
# Loop to parse XML for each row and create columns with field names
for i in range(len(df)):
    # For current row, parse the XML
    parsed = ET.fromstring(df.at[i, 'AUDITRECORD'])
    # For each child in parsed XML, pull out the new value
    for child in parsed:
        # Pull out the name of the updated field.
        name = child.get('name')
        # Enter the new value into a column with the field name.
        df.at[i,name] = child[-1].text
print(df)
# Exports the DF to a CSV
df.to_csv('testoutput.csv')