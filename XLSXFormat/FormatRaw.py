# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:22:46 2016

@author: mikew
"""

import pandas as pd
import datetime

now = datetime.datetime.now()

FileList = ['First', 'Second', 'Third', 'Fourth']

d = {}

for File in FileList:
    d[File] = pd.read_excel(File+'.xlsx')

writer = pd.ExcelWriter('Final.xlsx', engine='xlsxwriter')
workbook = writer.book
format1 = workbook.add_format()
format1.set_text_wrap()
format1.set_align('top')

for Key in d.keys():
#    print(Key)
#    print(d[Key].columns)
    for x in d[Key].columns:
#      print(x + ': ' + str(d[Key][x].dtype))
       if d[Key][x].dtype == 'datetime64[ns]':
#           print('ISDATE')
           d[Key][x] = d[Key][x].dt.strftime('%m/%d/%Y')
#           print('UPDATED- ' + x + ': ' + str(d[Key][x].dtype))
#       else:
#          print('NOTDATE')

for File in FileList:
    d[File].to_excel(writer, sheet_name = File, index=False)
    worksheet = writer.sheets[File]
    worksheet.set_column('A:B',5,format1)
    worksheet.set_column('C:F',50,format1)    

#for File in FileList:
#    print(File + ': ' + str(len(d[File])))
    
writer.save()

frames = d.values()
#print(frames)
result = pd.concat(frames)
#print(result['Email'])
BCCList = result['Email'].to_frame()

dwriter = pd.ExcelWriter('Distribution.xlsx', engine='xlsxwriter')
dworkbook = dwriter.book
dworksheet1 = dworkbook.add_worksheet('Totals')
BCCList.to_excel(dwriter, sheet_name = 'UserBCCList', index=False)
dworksheet3 = dworkbook.add_worksheet('UserEmail')
dworksheet4 = dworkbook.add_worksheet('LeaderEmail')


for i in range(len(FileList)):
    dworksheet1.write(i,0,FileList[i])
    dworksheet1.write(i,1,len(d[FileList[i]]))

TypeResults = ''
for i in range(len(FileList)):
    TypeResults += (FileList[i] + ': ' + str(len(d[FileList[i]])) + '\r\n')
print(TypeResults)

#dworksheet1.write(0,0,TypeResults)

dworksheet3.write(0,0,'To: ')
dworksheet3.write(0,1,'A.com; B.com; C.com')
dworksheet3.write(1,0,'BCC: ')
dworksheet3.write(1,1,'See UserBCCList worksheet')
dworksheet3.write(2,0,'Subject: ')
dworksheet3.write(2,1,'This Is the Subject ' + now.strftime("%Y-%m-%d"))
dworksheet3.write(3,0,'Body: ')
dworksheet3.write(3,1,'Dear everyone,\r\n\r\nThis is the email body.\r\n\r\nThese are the results:\r\n'+TypeResults+'\r\n\r\nThis is still the body.')

dwriter.save()

'''
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
'''