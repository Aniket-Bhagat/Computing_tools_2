print """------------------------------------------------------
|     Recursive function for Factorial of number     |
------------------------------------------------------\n"""

print """Note:
Maximum Recursive limit of python is upto 997
so give number upto 997 else it will give
RuntimeError: maximum recursion depth exceeded"""

def factorial(n):
	return (1 if n==0 else n*(factorial(n-1)))

number=input("\nEnter a number : ")

print "\n------------------------------------------------------"
print "Factorial of",number,"is :",factorial(number)
print "------------------------------------------------------"