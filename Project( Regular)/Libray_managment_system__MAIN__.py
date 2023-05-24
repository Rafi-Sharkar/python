#***********************************************************************************************_____all Functions___and lsit and dictionary
#All list 

L_books=["bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r","bangla","english","math","physics","python","biology","java","r"]
U_admin=[["Rafi"],["0777"]]
U_a_n=U_admin[0]
U_a_p=U_admin[1]
U_member=[["Alif"],["0111"]]
U_m_n=U_member[0]
U_m_p=U_member[1]

#price dictionary

price_dict={
    "bangla":150,
    "english":250,
    "math":320,
    "physics":380,
    "python":720,
    "biology":220,
    "java":650,
    "r":480
            }

#sign_up

def sign_up():                  #completed
    global U_a_n,U_a_p,U_m_n,U_m_p,U_admin
    print("Please fill up the information >>>>>>\n")
    sum=input("Enter your name ::: ")
    sup=input("Enter your password ::: ")
    sus=input("Enter your indentity ::: ")
    if sus in ("A","a","Admin","admin"):
        U_a_n.append(sum)
        U_a_p.append(sup) 
        print("Your registation has been completed.. as a admin. :) :) :)")               
    elif sus in ("M","m","Member","member"):
        U_m_n.append(sum)
        U_m_p.append(sup)
        print("Your registation has been completed.. as a member. :) :) :)\n")               


#sign_in and add book and price

def sign_in():                  #completed
    global L_books,U_admin,price_dict,U_a_n,U_a_p,U_m_n,U_m_p
    while True: 
       sum1=input("Enter your name ::: ")
       sup1=input("Enter your password ::: ")
       sus1=input("Enter your indentity ::: ")
       if sus1 in ("A","a","Admin","admin"):           
           if sum1 in U_a_n and sup1 in U_a_p: 
               while True:
                   b_n=(input("Enter the book name which you want to add ? :::  "))
                   b_num=int(input("How much book do you want to add ? :::  "))
                   b_pri=int(input("How much price of this book ? :::  "))
                   o=input("Do you want to add more books (y/n)::: ")
                   update_dict={
                        b_n:b_pri,
                                }
                   price_dict.update(update_dict)
                   for i in range (b_num):
                      L_books.append(b_n)
                   print(L_books)
                   if o.upper() == "Y":
                       continue
                   elif o.upper() == "N":
                      print("Bye :) :) :)")
                   break
           else:
               print("Try again")
               break
       else:
           print("Try again")
           break
       break


#view all books

def view_a_b():                  #completed
  global L_books
  while True:
      L_books_set = set(L_books)
      L_books_set_L=list(L_books_set)
      print(L_books_set_L)
      i=1
      for i in range(len(L_books_set_L)):
          print(f"The name of the book is '{L_books_set_L[i]}' and it's amount is  '{L_books.count(L_books_set_L[i])}'.")
      break
 

#Search book

def search():                  #completed
    global L_books
    while True: 
      sh=input("Which book do you want to find? ::: ")
      L_books_set = set(L_books)
      L_books_set_L=list(L_books_set)
      i=1
      for i in range(len(L_books_set_L)):
          if (L_books_set_L[i] == sh):
              print(f"The name of the book is '{L_books_set_L[i]}' and it's amount is  '{L_books.count(L_books_set_L[i])}'.")
      o1=input("Do you want to find any more book? (y/n) ::: ")
      if o1.upper() == "Y":
         continue
      elif o1.upper() == "N":
           print("Bye :) :) :)")
      break


#sign_in and Remove book 

def remove():                  #completed
    global L_books,U_admin
    while True:
       sum1=input("Enter your name ::: ")
       sup1=input("Enter your password ::: ")
       sus1=input("Enter your indentity ::: ")
       if sus1 in ("A","a","Admin","admin"):           
           if sum1 in U_a_n and sup1 in U_a_p:            
                while True: 
                 L_books_set = set(L_books)
                 L_books_set_L=list(L_books_set)
                 print(L_books_set_L)
                 ren=input("Which book do you want to remove? ::: ")         
                 renum=int(input("How many book do you want to remove? ::: "))      
                 for i in range(renum):
                     for j in range(len(L_books_set_L)):
                         if (L_books_set_L[j] == ren):                           
                            L_books.remove(ren)
                 o1=input("Do you want to remove any more book? (y/n) ::: ")
                 if o1.upper() == "Y":
                    continue
                 elif o1.upper() == "N":
                      print("Bye :) :) :)")
                 break
                
           else:        
               print("Try again")
               break
       else:
           print("Try again")
           break
       break


#Buy books and discount

def buy_book():
    global L_books,price_dict,U_a_n,U_a_p,U_m_n,U_m_p
    while True:
        sus1=input("what's your status ? :::")
        if sus1 in ("C","c","Customer","customer"): 
               while True:                  
                  b_n=(input("Which book do you want to buy ? :::  "))
                  b_num=int(input("How many book do you want to buy ? :::  "))
                  o=input("Do you want to add more books (y/n)::: ")
                  if b_n in list(price_dict.keys()):
                     total_pri=((price_dict[b_n])*b_num)                                      
                     print(f"Your bill is {total_pri}tk.\n")
                  for i in range (b_num):
                     L_books.remove(b_n)
                  if o.upper() == "Y":
                      continue
                  elif o.upper() == "N":
                     print("Bye :) :) :)")
                  break


        elif  sus1 in ("A","a","Admin","admin"):
            sun1 = input("Enter your name ::: ")
            sup1 = input("Enter your passward ::: ")
            if sun1 in U_a_n and sup1 in U_a_p :
                    while True:
                       b_n=(input("Which book do you want to buy ? :::  "))
                       b_num=int(input("How many book do you want to buy ? :::  "))
                       o=input("Do you want to add more books (y/n)::: ")
                       if b_n in list(price_dict.keys()):
                            total_pri=((price_dict[b_n])*b_num*.7)
                            print(f"You got 30% off.Your bill is {total_pri}tk\n")
                       for j in range (b_num):
                          L_books.remove(b_n)
                       if o.upper() == "Y":
                           continue
                       elif o.upper() == "N":
                          print("Bye :) :) :)")
                       break
        
        elif sus1 in ("M","m","Member","member"):
            sun2 = input("Enter your name ::: ")
            sup2 = input("Enter your passward ::: ")
            if sun2 in U_m_n and sup2 in U_m_p :
                while True:
                       b_n=(input("Which book do you want to buy ? :::  "))
                       b_num=int(input("How many book do you want to buy ? :::  "))
                       o=input("Do you want to add more books (y/n)::: ")
                       if b_n in list(price_dict.keys()):
                            total_pri=((price_dict[b_n])*b_num*.85)
                            print(f"You got 15% off.Your bill is {total_pri}tk\n")
                       for k in range (b_num):
                          L_books.remove(b_n)
                       if o.upper() == "Y":
                           continue
                       elif o.upper() == "N":
                          print("Bye :) :) :)")
                       break
        break



#****************************************************************************************______Main code


while True:  
  print(f"--------------------Welcome to our Library--------------------\n")
  print("##########>>>>>>>>>>_____Main menu of the library_____<<<<<<<<<<##########\n")
  print("1. New registation ")  #completed
  print("2. Add book ")  #completed
  print("3. View all book")  #completed
  print("4. Search book ")  #completed
  print("5. Remove book ")  #completed
  print("6. Buy  book ")  #completed
  print("7. Main menu\n")  #completed

  option1=input("Choose a option ?\t\n")               #Choose a option

  #1. New registation
  if option1 == str(1):
    sign_up()
    continue
                  
  # 2.add book
  if option1 == str(2):
    print("1.Sign_up")
    print("2.Sign_in")
    print("3.Main menu")

    option1_1=input("")                     #Choose a option 

    if option1_1 == str(1):
        sign_up()
        continue
    if option1_1 == str(2):
        sign_in()
        continue
    if option1_1 == str(3):
        continue

  # 3. View all book
  if option1 ==str(3):
      view_a_b()
      continue

  #4. Search the book
  if option1  == str(4):        #it run very fast see full screen terminal
      search()
      continue

  #5. Remove book 
  if option1 == str(5):
      remove()
      continue

  #6. Buy  book  
  if option1 == str(6):
      print("Avalable books and it's price__\n", price_dict )
      buy_book()
      continue

  #7. Main menu
  if option1 == str(7):
    continue

  break

#****************************************************************************************______test items

# OUTPUT*********************************************************************************************
