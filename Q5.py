print """------------------------------------------------------
|    Traingle is right angle traingle or not	     |
------------------------------------------------------\n"""

print """           A
          /|
         / |
        /  |
       /   |
      /    |
   C /_____| B\n\nGive input for length of sides of  triangle"""

AB=input("Length of Side A-B : ")
BC=input("Length of Side B-C : ")
AC=input("Length of Side A-C : ")


def check(x,y,z):
  if (x**2+y**2)==z**2:
    return "Traingle is Right Angled Traingle"
  else:
    return "Traingle is not a Right Angled Traingle"

if AB==0 and BC==0 and AC==0:
  print "\nAll sides can't be zero"
elif AB==AC or BC==AC:
  print """\nLength of Hypotenuse can't be equal to either side
Then other side becomes equal to 0

Not a Right Angled Traingle"""
else:
  print '\n',check(AB,BC,AC)