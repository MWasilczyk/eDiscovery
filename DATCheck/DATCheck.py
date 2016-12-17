"""
Created on Fri Dec 16 22:20:18 2016

@author: mikew
"""

import pandas as pd
import glob
# import chardet

DATList = glob.glob('./*.dat')
print(DATList)

'''
# Check encoding of file - MAY BE SLOW
with open(DATList[0], 'rb') as f:
    DATEncoding = chardet.detect(f.read())
    print(DATEncoding)
'''

DATFile = pd.read_csv(DATList[0], sep='|', quotechar = '^', encoding='cp1252')
print(DATFile.describe())
print('\r\n########################\r\n')

print(list(DATFile))
print('\r\n########################\r\n')

print('Length of DAT: ' + str(len(DATFile)))
print('\r\n########################\r\n')

DATSummary = pd.DataFrame()
for column in DATFile:
#    try:    
#        FirstRecord = DATFile[column].iloc[DATFile[column].first_valid_index()]
#    except:
#        FirstRecord = 'UNAVAILABLE'
    DATFile[column] = DATFile[column].astype('str')
    try:
        RecordCount = DATFile[DATFile[column] != 'nan'][column].count()
    except:
        RecordCount = 'UNAVAILABLE'
    try: 
        UniqueCount = DATFile[column].nunique()
    except:
        UniqueCount = 'UNAVAILABLE'
    try:
        MostCommon = DATFile[DATFile[column] != 'nan'][column].value_counts().idxmax()
    except:
        MostCommon = 'UNAVAILABLE'
    try:    
        MinResult = min(DATFile[DATFile[column] != 'nan'][column])
    except:
        MinResult = 'UNAVAILABLE'
    try:    
        MaxResult = max(DATFile[DATFile[column] != 'nan'][column])
    except:
        MaxResult = 'UNAVAILABLE'        
    FieldSummary = {'Field':column,
                    'Count':RecordCount,
                    'CountUnique':UniqueCount,
                    'Most Common':MostCommon,
#                    'First non-null':FirstRecord,
                    'Minimum':MinResult,
                    'Maximum':MaxResult}
    DATSummary = DATSummary.append(FieldSummary, ignore_index=True)
    
writer = pd.ExcelWriter('Summary.xlsx', engine='xlsxwriter')
workbook = writer.book
DATSummary.to_excel(writer, sheet_name = 'Full', index=False)
writer.save()
