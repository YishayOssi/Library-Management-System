import uuid

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.isbn = str(uuid.uuid4())[:4]
        self.is_available = True

    def __str__(self):
        return f"title: {self.title} author: {self.author} isbn: {self.isbn} is_available: {self.is_available}"

    def __repr__(self):
        return self.__str__()

    
