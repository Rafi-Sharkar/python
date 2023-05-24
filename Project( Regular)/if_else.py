 x=int(input("Please enter a number: "))
if x> 10:
  if x>20:
    if x>30:
      if x>40:
        print("MT40")
      else: print("MT30")
    else: print("MT20")
  else: print("MT10")
else: print("MT0")


# Know Your Gread

g=int(input("Type your marks"))

if (g>100):
 print("Type the correct marks")
elif (100>g>80):
 print("A+")
if (80>g>75):
 print("A")
elif (75>g>70):
 print("A-")
if (70>g>65):
 print("B+")
elif (g<65):
 print("Fail")