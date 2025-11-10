from book import Book
from user import User
class Library:
    def __init__(self):
       self.list_of_books = []
       self.list_of_users = []


    def add_book(self,book:Book):
        self.list_of_books.append(book)


    def add_user(self,user:User):
        self.list_of_users.append(user)


    def borrow_book(self,user_id, book_isbn):
        #בודק אם ספר קיים והאם תפוס או פנוי
        for i in self.list_of_books:
            #אם ספר קיים
            if book_isbn == i.isbn:
                #אם מושאל
                if i.is_available == False:
                    print("תפוס")
                    return
                #אם לא מושאל
                else:
                    #מחפש משתמש
                    for j in self.list_of_users:
                        if user_id == j.id:
                            #מוסיף ספר למשתמש והופך ספר ללא זמין
                            j.borrowed_books.append(i)
                            i.is_available = False
                            print("מושאל בהצלחה")
                            return
        #אם הגיע לכאן ספר או משתמש לא קיים
        print("משתמש או ספר לא קיים")


    def return_book(self, user_id, book_isbn):
         for user in self.list_of_user:
             #האם המשתמש קיים 
             if user.id == user_id:
                for book in user.borrowed_books:
                    #האם הספר קיים ברשימת ההשאלות שלו
                    if book.isbn == book_isbn:
                        book.is_available = True
                        user.borrowed_books.remove(book)
                    else:
                        print("The book does not exist in the system")
             else: 
                 print("The user does not exist.")  


    def list_available_books(self):
        for i in self.list_of_books:
            if i.is_available == True:
                print(i)


    def search_book(self,title):
        for i in self.list_of_books:
            if i.title == title:
                return True
        return False






      
        


    
  
    

   







    
    
