#Exercise 6: Library Books

#Requirements:

    #Create a Book class with instance variables title and author.
    #Add a class variable library_name representing the library's name.
    #Add a class variable total_books_borrowed to keep track of how many books have been borrowed.
    #Create a method to mark a book as borrowed, and increment total_books_borrowed each time a book is borrowed.
    #Print the library name and the total number of books borrowed.

class Book:
    library_name = "National Library"
    total_books_borrowed = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrow = False
    def borrow_check(self):
        if self.borrow == False:
            print(f"This {self.title} book is available, do you want to borrow?")
            choice = input().lower()
            if choice == "yes":
                print(f"You have successfully borrow {self.title}")
                Book.total_books_borrowed += 1
                self.borrow = True
            else:
                print("There are another books for you to choose")
        else:
            print(f"Sorry, the book {self.title} has been already borrowed, choose another one")

book1 = Book("How to Win & Influence Friends", "Dale Carnegie")
book2 = Book("Rich Dad, Poor Dad", "Robert Kiyosaki")
book1.borrow_check()
book2.borrow_check()
book1.borrow_check()
print("Total book borrowed:", Book.total_books_borrowed)


















































    






















