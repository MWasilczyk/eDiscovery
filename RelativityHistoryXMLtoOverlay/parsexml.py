# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:44:17 2016

To do:
1. Create separate DAT overlay files for each field (DOCID + field)
2. Check for a document with multiple updates to the same field, only keep
    latest value.

"""

import pandas as pd
import xml.etree.ElementTree as ET

inputfile = 'testcsv.csv'

# Reads CSV into memory as a dataframe, beware quotechar/CSV defaults
df = pd.read_csv(inputfile, quotechar='^')
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