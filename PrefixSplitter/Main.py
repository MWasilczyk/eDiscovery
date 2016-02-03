'''
Designed to take a list of bates numbers and create a list of prefixes.
'''
import pandas as pd

def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def line_check(c):
    for x in range(len(c)):
        if is_int(c[x]) and is_int(c[x+1]) and is_int(c[x+2]) and is_int(c[x+3]) and is_int(c[x+4]):
            return c[0:x] 

def prefixes(filename):
    lines = open(filename).readlines()
    i = []
    for c in lines:
        i += [line_check(c)]
    return i

s = pd.read_csv('saltvpepper.csv',sep='|',quotechar='^')
#s = prefixes('TestPrefixes.txt')
#s = pd.Series(s)
print s
s = s.value_counts()
print s