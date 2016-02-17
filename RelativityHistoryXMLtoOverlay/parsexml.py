# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:44:17 2016

@author: mikew
"""

import pandas as pd
import xml.etree.ElementTree as ET


print('=====================XML=====================')
tree = ET.parse('test.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)
    print(child[-1].text)

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
    
print('=====================CSV-DATAFRAME=====================')

df = pd.read_csv('testcsv.csv', quotechar='^')
#print(df)
df['test'] = ''
#print(df['AUDITRECORD'])
for i in range(len(df)):
    parsed = ET.fromstring(df.at[i, 'AUDITRECORD'])
    df.at[i,'test'] = i
    for child in parsed:
        name = child.get('name')
        df.at[i,name] = child[-1].text
#print(df.at[0, 'AUDITRECORD'])    
print(df)
df.to_csv('testoutput.csv')