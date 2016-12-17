"""
Created on Fri Dec 16 22:20:18 2016

@author: mikew
"""

import pandas as pd
import glob
# import chardet

# Get list of .DAT files in current directory
DATList = glob.glob('./*.dat')
print(DATList)
print('\r\n########################\r\n')

# Optional section to check encoding of the DAT
'''
# Check encoding of file - MAY BE SLOW
with open(DATList[0], 'rb') as f:
    DATEncoding = chardet.detect(f.read())
    print(DATEncoding)
'''

# Read the DAT file into a dataframe
DATFile = pd.read_csv(DATList[0], sep='|', quotechar = '^', encoding='cp1252')

# Print the field names from the DAT
print(list(DATFile))
print('\r\n########################\r\n')

# Print number of rows
print('Length of DAT: ' + str(len(DATFile)))

# Initialize DataFrame with column order
DATSummary = pd.DataFrame(columns=['Field',
                                   'Count',
                                   'Unique',
                                   'MinLength',
                                   'MaxLength',
                                   'Most Common',
                                   'Minimum',
                                   'Maximum'])

# Primary loop: reports stats for each series
for column in DATFile:
    # Convert series to string
    DATFile[column] = DATFile[column].astype('str')
    # Remove null values
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
    # Create dictionary of field names/calculated variables
    FieldSummary = {'Field':column,
                    'Count':RecordCount,
                    'Unique':UniqueCount,
                    'MinLength':MinLength,
                    'MaxLength':MaxLength,
                    'Most Common':MostCommon,
                    'Minimum':MinResult,
                    'Maximum':MaxResult}
    # Adds dictionary as a row to the summary DataFrame
    DATSummary = DATSummary.append(FieldSummary, ignore_index=True)

# Creates a new Excel workbook
writer = pd.ExcelWriter('Summary.xlsx', engine='xlsxwriter')
workbook = writer.book

# Writes the summary DataFrame to the workbook
DATSummary.to_excel(writer, sheet_name = 'Full', index=False)

# General text format
format1 = workbook.add_format()
format1.set_text_wrap()
format1.set_align('left')
format1.set_align('top')

# Conditional formatting to highlight null values
format2 = workbook.add_format({'bold': 1, 
                               'italic': 1,
                               'bg_color': '#FFC7CE'})

# Applies general formatting and column width
worksheet = writer.sheets['Full']
worksheet.set_column('A:A',25,format1)
worksheet.set_column('B:E',10,format1)
worksheet.set_column('F:H',80,format1)  

# Applies conditional formatting for certain columns
worksheet.conditional_format('D2:F50', {'type':     'text',
                                        'criteria': 'containing',
                                        'value':    'NULL',
                                        'format':   format2})

# Saves and closes the workbook
writer.save()
