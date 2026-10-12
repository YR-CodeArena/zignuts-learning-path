class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_title):
        self.books.append(book_title)
        print("Book added successfully")

    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            print("Book removed")
        else:
            print("Book not found")

    def search_book(self, book_title):
        found = False
        for book in self.books:
            if book.lower() == book_title.lower():
                found = True
                break
        
        if found:
            print("Book is available in library")
        else:
            print("Book is not available")


lib = Library()
lib.add_book("Python Basics")
lib.add_book("Django for Beginners")
lib.search_book("python basics")
lib.remove_book("Python Basics")
lib.search_book("Python Basics")