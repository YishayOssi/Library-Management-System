import uuid
class Book:
    def __init__(self,title:str,author:str):
        self.title = title
        self.author = author
        self.isbn = uuid.uuid4()
        self.is_available = True
    def __str__(self):
        print( str(self.__dict__))
    
