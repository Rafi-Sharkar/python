'''
please create three lists and take N numbers of integers as input in those three different lists.
1. Print the total sum of all those variables of three lists.
2. find maximum and minimum from all three lists.
3. count the total number of even numbers in the list
4. Count the total number of odd numbers in the list


create necessary functions and finally submit the code in.ipynb file
'''
l1= [5,7,6,1,9,4,14,56,41,17,21]
l2= [3,6,9,4,0,8,11,13,19,27,31]
l3= [51,71,37,28,27,9,60,0,0,15]
while True:
  x=int(input("Enter the number into the list 1 ::: "))
  y=int(input("Enter the number into the list 2 ::: "))
  z=int(input("Enter the number into the list 3 ::: "))
  l1.append(x)
  l2.append(y)
  l3.append(z)
  check = input("Do you want to quit or start again? enter Y to restart or another key to end: ")
  if check.upper() == "Y":              #goto the initial state
    continue   
  print("Bye...")
  break 

print("The sum of those three Lists. \n")
s,p,a=0,0,0
for i in l1:
  s=s+i   
print(f"Sum of the list 1 is {s}")
for j in l2:
  p=p+j   
print(f"Sum of the list 2 is {p}")
for k in l3:
  # a=0
  a=a+k   
print(f"Sum of the list 3 is {a}")


print("The max and min value of those three Lists. \n")
l1.sort()
print(f"The max value of list 1 is {l1[-1]} and the min value of list 1 is {l1[0]}")
l2.sort()
print(f"The max value of list 2 is {l2[-1]} and the min value of list 2 is {l2[0]}")
l3.sort()
print(f"The max value of list 3 is {l3[-1]} and the min value of list 3 is {l3[0]}")

print("The even and odd value of those three Lists. \n")
l1e=[]
l1o=[]
l2e=[]
l2o=[]
l3e=[]
l3o=[]
for i in l1:
  if i%2 == 0:
    l1e.append(i)
  else:
    l1o.append(i)
print(f"The even number in the list 1 are :::{l1e}\t")
print(f"The odd number in the list 1 are :::{l1o}\t")

for f in l2:
  if f%2 == 0:
    l2e.append(f)
  else:
    l2o.append(f)
print(f"The even number in the list 1 are :::\t{l2e}")
print(f"The odd number in the list 1 are :::{l2o}\t")

for h in l3:
  if h%2 == 0:
    l3e.append(h)
  else:
    l3o.append(h)
print(f"The even number in the list 1 are :::\t{l3e}")
print(f"The odd number in the list 1 are :::{l3o}\t")


