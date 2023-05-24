# def Menu():
print(f"----------Welcome to our Library----------\n\n")
print(f"Give your identity_____.  [Admin(A),Member(M),Customer(C)]")
identity = input()

#****************************************************************************************
#All list 
L_books=[]
U_admin=[[],[]]
U_a_n=U_admin[0]
U_a_p=U_admin[1]
U_member=[[],[]]
U_m_n=U_member[0]
U_m_p=U_member[1]
#ALl basic function
def add():
    pass

def search():
    pass

def buy():
    pass

def discount():
    pass

def sign_up():      #completed
    sum=input("Enter your name ::: ")
    sup=input("Enter your password ::: ")
    sus=input("Enter your indentity ::: ")
    if sus is ("A","a","Admin","admin"):
        U_a_n.append(sum)
        U_a_p.append(sup)
    elif sus is ("M","m","Member","member"):
        U_m_n.append(sum)
        U_m_p.append(sup)
    else:
        pass

def sign_in():
    pass

def borrow():
    pass

def view_all():
    pass

if identity is ("A","a","Admin","admin"):
    sign_up()
    sign_in()
    pass

if identity is ("M","m","Member","member"):
    sign_up()
    sign_in()
    pass

if identity is ("C","c","Customer","customer"):
    pass


# OUTPUT*********************************************************************************************


