from tkinter import PAGES


class Book:
    def __init__(self, title, author, pages, current_page,):
        self.title = title
        self.author = author
        self.pages = pages
        self.page_number = 1
        self.current_page = current_page
        self.bookmark = 1

    def bookmark_page(self):
        self.bookmark = int(input("bookmark a page : "))

    def turn_page(self):
        if self.current_page >= self.pages:
            self.current_page = 1
        else:
            self.current_page += 1

    def select_page(self,):
        self.current_page = int(input("Select a page number: "))
    
    def __str__(self):
        return f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}"

    def __len__(self):
        return self.pages

my_book = Book("A great book", "me", 198, 1)
print(my_book)

my_book.bookmark_page()
print(my_book.bookmark)
my_book.turn_page() 
print(my_book.current_page)
my_book.select_page()
my_book.turn_page()
print(my_book.current_page)

