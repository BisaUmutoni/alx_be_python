class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library():
    def __init__(self):
        self._books = []
    def add_book(self, Book):
        self._books.append(Book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return True
        return False

    def return_book(self, title):
        for Book in self._books:
            if Book.title == title:
                Book._is_checked_out = False
                return True
        return False
    
    def list_available_books(self):
        available_books = [Book for Book in self._books if not Book._is_checked_out]
        return available_books