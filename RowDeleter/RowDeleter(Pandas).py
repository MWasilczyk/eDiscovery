# -*- coding: utf-8 -*-
'''
Parameters:
1. One or directory of CSV files to process.
2. A text file containing a list of terms to exclude.
3. The name of the CSV column header to search for the terms.
4. A desired prefix for the newly made files.

Actions:
1. Prompt for single file or directory.
2. If single file, prompt for filename.
3. Prompt for exclusion file.
4. Prompt for CSV column header.
5. Prompt for desired prefix.
6. Pass four parameters into function.
7. For each CSV file, create dataframe, remove rows containing an excluded term.
8. Write new CSV file from updated dataframe.
'''

import glob
import pandas as pd


print 'Please ensrue that this script is in the directory with the file(s) you wish to clean.'

# x = current file, y = file of names to remove, z = column header to check, a = new filename prefix
def removelines(x, y, z, a):
    datanames = open(y).read().splitlines()
    df = pd.DataFrame.from_csv(x, index_col=False)
    df = df[~df[z].isin(datanames)]
    # Create new file.
    df.to_csv(a + x, index=False)

# Determine if single file or directory.
while True:
    renamethis = raw_input('Please enter "all" to rename all CSVs in this directory, or "single" to name a single file: ')
    if renamethis == 'all':
        # Creates list of all CSVs in directory
        files = [f for f in glob.glob("*.csv")]
        break
    elif renamethis == 'single':
        # Loop checks for valid filename.
        while True:
            try:
                files = raw_input('Please enter the filename with extension: ')
                open(files)
                break
            except:
                pass
            print 'Please ensure the file and script are in the same directory.'
        break
    else:
        print 'Please enter choice without quotation marks.'

# Determine the terms to be excluded.
while True:
    # Ensure valid file.
    try:
        removethese = raw_input('Please enter a text file (with extension) containing a list of strings to exclude: ')
        open(removethese)
        break
    except:
        pass
    print "Please ensure the file and script are in the same directory."

# Prompt for CSV column name and desired prefix.
columnname = raw_input('Please enter the CSV column name to search: ')
newprefix = raw_input('Please enter a prefix for the new filename(s): ')

# Check to see if single file or directory. Loop if directory (list)
if type(files) == list:
    for csv in files:
        removelines(csv, removethese, columnname, newprefix)
elif type(files) == str:
    removelines(files,removethese, columnname, newprefix)