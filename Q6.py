print """------------------------------------------------------
|    Print numbers having only even digits in it     |
------------------------------------------------------\n"""

x,y=input("Input range for numbers seperated by comma(,) : ")

def give(i):
	number=str(i); count=0
	for j in number:
		if int(j)%2==0:
			count+=1
	if len(number)==count:
		return True
	else:
		return False

print "\nList of numbers having only Even Digits in it :"
print filter(lambda x: give(x),[i for i in range(x,y+1)])