print """------------------------------------------------------
|    Extract Binary numbers only divisible by 5      |
------------------------------------------------------\n"""
def check(n):
	binary=True
	for i in str(n):
		if i!='0' and i!='1':
			binary=False
			break
	if binary==True:
		if n%5==0 and n!=0:
			return n
	# 	else:
	# 		return 'Nothing'#print 'Not Divisible by 5'
	# else:
	# 	return 'Nothing'#print 'Not a binary'

print "Input each number seperated by comma (,)\ne.g. 1000,1010,125,1111,011101"
print "Give at least one number\n"
seq=input("Give your input :\n")

print "\n------------------------------------------------------"
try:
	print "Binary number(s) which are Divisible by 5 :"
	result=(map(lambda x: check(x),seq))
	result=list(x for x in result if x!=None)
	if result!=[]: print result
	else: print "None"
except TypeError:
	print check(seq)
print "------------------------------------------------------"