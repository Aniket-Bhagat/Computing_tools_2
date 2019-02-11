print """------------------------------------------------------
|     Recursive function to make String reverse      |
------------------------------------------------------\n"""

print """Note:
Maximum Recursive limit of python is upto 997
so give string of maximum length 997 else it will give
RuntimeError: maximum recursion depth exceeded"""

def rev(str1):
	return (str1 if str1=='' else rev(str1[1:])+str1[0])

string=raw_input("\nEnter your String : ")

print "\n------------------------------------------------------"
print "Reverse of string :", rev(string)
print "------------------------------------------------------"