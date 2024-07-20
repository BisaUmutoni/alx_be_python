class Book:
    def __init__(self, title, author):
        self.title = str (title)
        self.author = str (author)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
        
class EBook (Book):
        def __init__(self, title, author, file_size):
            super().__init__(title, author)
            self.file_size = int(file_size)
        def __str__(self):
         return f"{self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
        def __init__(self, title, author, page_count):
            super().__init__(title, author)
            self.page_count = (page_count)
            return f"{self.title}, {self.author}, {self.page_count}"
            
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)