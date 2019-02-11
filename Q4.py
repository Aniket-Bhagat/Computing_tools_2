print """------------------------------------------------------
|    Finding Common Elements From Given files	     |
------------------------------------------------------\n"""

import sys
from functools import reduce
files=sys.argv[1:]

def ComList(seq1,seq2):
	common=[i for i in seq1 if i in seq2]
	return set(common)

def common(names):
	data=[]
	for i in range(1,len(names)+1):
		data.append((open(names[i-1])).read().splitlines())
	product = reduce((lambda listx,listy: ComList(listx,listy)), data)
	return sorted(list(set(product)))

if common(files)==[]:
	print 'Nothing is Common in given files'
else:
	print 'Common Elements from given files are following :'
	print common(files)

print "------------------------------------------------------"