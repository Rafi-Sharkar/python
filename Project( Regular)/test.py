'''
def main():
    again = 'y'
    while again.lower() == 'y':
        num = 2
        total = 0
        while num <= 100:
            if num % 2 == 0:
                total = total + num
                num += 1
            else:
                num += 1
                
        print("Sum of even numbers between 2 and 100 is:", total)
        again = input("Do you want to run this program again[Y/n]?")

main()

'''

#2 Ways to Loop Back to the Beginning of a Program in Python
'''
while True:
  distance =  float(input("Enter the distance in kilometers: "))
  time = float(input("Enter the time in hours: "))
  speed = distance/time
  print("Speed is:", speed,"kph")
  check = input("Do you want to quit or start again? enter Y to restart or another key to end: ")
  if check.upper() == "Y": #go back to the top
    continue    
  print("Bye...")
  break #exit

#or

distance =  float(input("Enter the distance in kilometers: "))
time = float(input("Enter the time in hours: "))
speed = distance/time
print("Speed is:", speed,"kph")
'''

# while True:
#   distance =  float(input("Enter the distance in kilometers: "))
#   time = float(input("Enter the time in hours: "))
#   speed = distance/time
#   print("Speed is:", speed,"kph")
#   check = input("Do you want to quit or start again? enter Y to restart or another key to end: ")
#   if check.upper() == "Y": #go back to the top
#     continue    
#   print("Bye...")
#   break 

# x=int(input("Please enter a number: "))
# if x%2 ==0:
#   print("Even")
# else:
#   print("Odd")

#back to the previous state
'''
l4=[]
while True:
  x=int(input("Enter the integers ::: "))
  o=input("Do you want to try again (y/n)::: ")
  l4.append(x)
  if o.upper() == "Y":
    continue
  elif o.upper() == "N":
    print("Bye :) :) :)")
  break
'''
# while True:
#   x=int(input("Enter the integers ::: "))
#   o=input("Do you want to try again (y/n)::: ")
#   if o == str(6):
#     continue
#   elif o.upper() == "N":
#     print("Bye :) :) :)")
#     break
#   break

# a_list = [1, 2, 3, 3]
# converted_set = set(a_list)         #Convert `a_list` to a set
# print(converted_set)


# Python3 program to convert a 
# set into a list
# my_set = {'Geeks', 'for', 'geeks'}
  
# s = list(my_set)
# print(s)


# L_books = ["a","b","d","e","c","a","b","c","a","x","c"]
# # L_books= [1,5,1,4,6,9,7,4,6,4,57,6,4,3,1,45,4,5]

# L_books_set = set(L_books)
# L_books_set_L=list(L_books_set)
# print(L_books_set_L)
# for i in range(len(L_books_set_L)):
#   # print(L_books_set_L[i])
#   print(f"The name of the book is {L_books_set_L[i]} and it's amount is {L_books.count(L_books_set_L[i])}")
  
# nameList=["john","carter"]
# print(nameList[1][-2])

l=[1,5,4]
print(len(l))
