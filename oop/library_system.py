class Book:
    def __init__(self, title, author):
            self.title = str (title)
            self.author = str (author)
    def __str__(self):
        try:
            return f"Book: {self.title} by {self.author}"
        except Exception as e:
            print (f"The book is not available: {e}")
        
class EBook(Book):
        def __init__(self, title, author, file_size):
            super().__init__(title, author)
            self.file_size = int(file_size)
        def __str__(self):
            try:
                return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
            except Exception as e:
                print (f"The book is not available: {e}")

class PrintBook(Book):
        def __init__(self, title, author, page_count):
            super().__init__(title, author)
            self.page_count = int (page_count)
        def __str__(self):
            try:
                return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
            except Exception as e:
                print (f"The book is not available: {e}")
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
            
class LibrarySystemError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __repr__(self):
        return f"LibrarySystemError('{self.message}')"
    