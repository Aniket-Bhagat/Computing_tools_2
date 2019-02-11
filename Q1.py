print """------------------------------------------------------
|    Finding Common Elements From Given Sequences    |
------------------------------------------------------\n"""
print "Which Type of sequence you want to give:\n1. List\n2. Tuples\n3. String"
n=input("Give your choice number : ")

def ComList(seq1,seq2):
	common=[i for i in seq1 if i in seq2]
	return set(common)

def inp(x):
	seq=(raw_input()).split(x)
	return seq

def ComAlp(str1,str2):
	str1=list(''.join(str1))
	str2=list(''.join(str2))
	return [i for i in str1 if i in str2]

if (n==1 or n==2):
	print "\nInput each Element of Sequence seperated by comma (,)\ne.g. 1,2,3 or a,b,c\n"
	print "Give input for Sequence1 : \b"
	sequence1=inp(',')
	print "Give input for Sequence2 : \b"
	sequence2=inp(',')


	choice={1:["List",list(ComList(sequence1,sequence2)),sequence1,sequence2],
			2:["Tuple",tuple(ComList(sequence1,sequence2)),tuple(sequence1),tuple(sequence2)]}

	print "\n------------------------------------------------------"
	print choice[n][0],"1 :",choice[n][2],'\n',choice[n][0],"2 :",choice[n][3]
	print "Common elements from given",choice[n][0]+"s :",choice[n][1]
	print "------------------------------------------------------"


elif (n==3):
	print "\nInput string as sentance where EOS is '\\n'"
	print "\nGive input for String1 : "
	string1=inp(' ')
	print "Give input for String2 : "
	string2=inp(' ')

	print "\n------------------------------------------------------"
	print "Common words from given two strings :\n",list(ComList(string1,string2))

	print "Common Alphabets set from given two strings :\n",list(set(ComAlp(string1,string2)))
	print "------------------------------------------------------"

else:
	print "\nSorry..!!\nChoice number not listed here"