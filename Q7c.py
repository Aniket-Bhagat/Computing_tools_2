print """------------------------------------------------------
|     Sum of first 'n' numbers using recursion       |
------------------------------------------------------\n"""

print """Note:
Maximum Recursive limit of python is upto 997
so give number upto 997 else it will give
RuntimeError: maximum recursion depth exceeded"""

def add(n):
	return(0 if n==0 else n+(add(n-1)))

number=input("\nEnter value for 'n' :")

print "\n------------------------------------------------------"
print "Sum of first",number,"numbers :",add(number)
print "------------------------------------------------------"