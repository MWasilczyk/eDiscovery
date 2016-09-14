# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 20:57:41 2016



@author: mikew
"""
import glob

f = glob.glob('*.txt')
print(f)

finalresults = open('FinalResults.csv', 'w')
finalresults.write('"Server Name","Protocol","Renegotiation supported?"\n')

for file in f:
    csvline = '"' + file.split('-')[0] + '","'
    currentfile = open(file, 'r').readlines()
    ProtocolCheck = 0
    for line in currentfile:
        if '    Protocol  :' in line:
            csvline += line.split(': ')[-1].split('\n')[0] + '","'
            ProtocolCheck += 1
    if ProtocolCheck == 0:
        csvline += '","'
    if 'Secure Renegotiation IS supported\n' in currentfile:
        csvline += 'Secure Renegotiation IS supported"'
    elif 'Secure Renegotiation IS NOT supported\n' in currentfile:
        csvline += 'Secure Renegotiation IS NOT supported"'
    else:
        csvline += 'TEST INCONCLUSIVE"'
    finalresults.write(csvline +'\n')
    
finalresults.close()    

#print(resultslines)

