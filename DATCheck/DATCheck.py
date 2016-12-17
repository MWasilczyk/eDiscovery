"""
Created on Fri Dec 16 22:20:18 2016

@author: mikew
"""

import pandas as pd
import glob
# import chardet

DATList = glob.glob('./*.dat')
print(DATList)
print('\r\n########################\r\n')

'''
# Check encoding of file - MAY BE SLOW
with open(DATList[0], 'rb') as f:
    DATEncoding = chardet.detect(f.read())
    print(DATEncoding)
'''

DATFile = pd.read_csv(DATList[0], sep='|', quotechar = '^', encoding='cp1252')
#print(DATFile.describe())
#print('\r\n########################\r\n')

print(list(DATFile))
print('\r\n########################\r\n')

print('Length of DAT: ' + str(len(DATFile)))

DATSummary = pd.DataFrame(columns=['Field',
                                   'Count',
                                   'Unique',
                                   'MinLength',
                                   'MaxLength',
                                   'Most Common',
                                   'Minimum',
                                   'Maximum'])

for column in DATFile:
    DATFile[column] = DATFile[column].astype('str')
    ThisSeries = DATFile[DATFile[column] != 'nan'][column]
    try:
        RecordCount = ThisSeries.count()
    except:
        RecordCount = 'NULL'
    try: 
        UniqueCount = ThisSeries.nunique()
    except:
        UniqueCount = 'NULL'
    try:
        MinLength = min(ThisSeries.str.len())
    except:
        MinLength = 'NULL'
    try:
        MaxLength = max(ThisSeries.str.len())
    except:
        MaxLength = 'NULL'
    try:
        MostCommon = ThisSeries.value_counts().idxmax()
        MostCommon = '[' + str(max(ThisSeries.value_counts())) +'] ' + MostCommon
    except:
        MostCommon = 'NULL'
    try:    
        MinResult = ThisSeries.min()
    except:
        MinResult = 'NULL'
    try:    
        MaxResult = ThisSeries.max()
    except:
        MaxResult = 'NULL'        
    FieldSummary = {'Field':column,
                    'Count':RecordCount,
                    'Unique':UniqueCount,
                    'MinLength':MinLength,
                    'MaxLength':MaxLength,
                    'Most Common':MostCommon,
                    'Minimum':MinResult,
                    'Maximum':MaxResult}
    DATSummary = DATSummary.append(FieldSummary, ignore_index=True)

writer = pd.ExcelWriter('Summary.xlsx', engine='xlsxwriter')
workbook = writer.book
DATSummary.to_excel(writer, sheet_name = 'Full', index=False)

format1 = workbook.add_format()
format1.set_text_wrap()
format1.set_align('left')
format1.set_align('top')

format2 = workbook.add_format({'bold': 1, 
                               'italic': 1,
                               'bg_color': '#FFC7CE'})

worksheet = writer.sheets['Full']
worksheet.set_column('A:A',25,format1)
worksheet.set_column('B:E',8,format1)
worksheet.set_column('F:H',80,format1)  

worksheet.conditional_format('D2:F50', {'type':     'text',
                                        'criteria': 'containing',
                                        'value':    'NULL',
                                        'format':   format2})

writer.save()
