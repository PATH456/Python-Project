#Project: Library Management System

#Objective: Create a class to manage books in a library, including adding books, calculating overdue fines, and maintaining library-wide settings.

#Requirements:

 #   Class Methods:
  #      set_fine_rate: Modify the fine rate for overdue books. This affects all books.
   #     add_book: Create new books with default values and add them to the library collection.

    #Static Methods:
     #   calculate_fine: Compute the fine for overdue books based on the number of overdue days and the fine rate.
      #  is_valid_isbn: Validate the ISBN of a book to ensure it follows a standard format.

#    Instance Methods:
 #       checkout: Mark a book as checked out and record the checkout date.
  #      return_book: Mark a book as returned and compute any overdue fines.
class Library:
    fine_rate = 0.1

    def __init__(self, name, overdue_check, price_borrow, days_overdue):
        self.name = name
        self.overdue_check = overdue_check
        self.price_borrow = price_borrow
        self.days_overdue = days_overdue
        self.status = False


    @classmethod
    def set_fine_rate(cls, amount):
       cls.fine_rate = amount
    @classmethod
    def add_book(cls, name, overdue_check, price_borrow, days_overdue):
        return cls(name, overdue_check, price_borrow, days_overdue)

    @staticmethod
    def calculate_fine(price_borrow, days_overdue):
        return Library.fine_rate * days_overdue * price_borrow
    @staticmethod
    def is_valid_isbn(isbn):
        if len(isbn) == 13 and isbn.isdigit():
            print("This is a valid isbn")
        else:
            print("This is not a valid isbn")

    def check_out(self):
        if not self.status:
            print("This book is available, do you want to borrow? ")
            choice = input().lower()
            if choice == "yes":
                self.status = True
                print("You have successfully borrowed this book, please remember to return it on time")
            else:
                print("It's okay, we still have many other books for you to choose")
        else:
            print("Sorry, this book is not available")

    def return_book(self):
        if self.overdue_check == "yes":
            fine = self.calculate_fine(self.price_borrow, self.days_overdue)
            print(f"This book is returned late, you have to pay an additional fine of {fine}")
        else:
            print("This book is returned on time. Thank you!")

book1 = Library.add_book("Never eat out alone", "no", 500, 0)
book2 = Library.add_book("Deep work", "yes", 200, 5)
book3 = Library.add_book("Adventure of cats", "yes", 650, 10)

book2.check_out()
book2.return_book()
print(book2.calculate_fine(200, 5))























































































    






















