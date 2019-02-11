print """------------------------------------------------------
|    Function to convert Decimal number to Binary    |
------------------------------------------------------\n"""

def makebinary(n):
	if n==0:
		return 0
	else:
		empty=[]
		while(n>0):                              
			m=n%2
			n=n/2
			empty.append(str(m))
		empty=''.join(empty)
		return(empty[::-1])


number=input('Enter a Decimal number : ')
print "\n------------------------------------------------------"
print 'Binary equivalent is :',makebinary(number)
print "------------------------------------------------------"