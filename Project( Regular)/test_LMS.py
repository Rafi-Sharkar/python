from _typeshed import Self


class Library:
    def __init(self,list,name):
        self.booklist = list
        self.name = name
        self.lendDict={}

    def displayBooks(self):
        print(f"We have following books in our Library")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book.user})
            print("Lender-Book Database has been updated. you can take the book now.")
        else:
            print("Book is allready in use by {self.lend.Dict[book]}")

    def aaddBook(self,book):
        self.booklist.append(book)
        print("book has been added to your list")

    def returnBook(self,book):
        self.leanDict.pop(book)

if __name__=='__main__':
    dnyanesh=Library(["Python","C++","Java","machinelearning"])
    while(True):
        print(f"welcome to the {dnyanesh.name}library. Enter your choice to continue")
        print("1.Display books")
        print("2.Lend book")
        print("3.Add book")
        print("4.Return book")
        user_choice=input()
        if user_choice not in ["1","2","3","4"]:
            continue
        else:
            user_choice=int(user_choice)
        
        if user_choice==1:
            dnyanesh.displayBook()
        elif user_choice==2:
            book=input("Enter the name of the book you want to lend::")
            user=input("Enter your name::")
            dnyanesh.lendBook(user,book)

        elif user_choice==3:
            book=input("Enter the name of the book doyou want to add::") 
            dnyanesh.returnBool(book)

        elif user_choice ==4:
            book=input("Enter the name of the book you want to return::")
            dnyanesh.returnBook(book)
        
        else:
            print("Not a valid option")

        print("Press Q to quit and C to continue")
        user_choice2=""
        while(user_choice2!="C" and user_choice2!="Q"):
            user_choice2=input()
            if user_choice2 =="Q":
                exit()
            if user_choice2 == "C":
                continue

            

    

