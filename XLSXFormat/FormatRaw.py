# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:22:46 2016

@author: mikew
"""

import pandas as pd

xl = pd.ExcelFile('raw.xlsx')
SheetNames = xl.sheet_names

d = {}
for Sheet in SheetNames:
    print(Sheet)
    try:
        d[Sheet] = xl.parse(Sheet)
    except:
        d[Sheet] = 'Hello'

#print(d)

writer = pd.ExcelWriter('Final.xlsx', engine='xlsxwriter')
workbook = writer.book
format1 = workbook.add_format()
format1.set_text_wrap()
format1.set_align('top')
format2 = format1
format2.set_num_format('mm/dd/yy')


#print(d['Second'])
print(d['First'].dtypes)

#d['First']['Date'].apply(lambda x: x.strftime('%Y%m%d'))
#d['First']['Date'].dt.strftime('%d%m%Y')
d['First']['Date'] = d['First']['Date'].dt.strftime('%m/%d/%Y')

print(d['First'].dtypes)

for Sheet in SheetNames:
    d[Sheet].to_excel(writer, sheet_name = Sheet, index=False)
    worksheet = writer.sheets[Sheet]
    worksheet.set_column('A:B',5,format1)
    worksheet.set_column('C:C',50,format1)

writer.save()