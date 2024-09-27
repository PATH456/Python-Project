#Encapsulation

class Library:
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_new_name(self, new_name):
        self.__name = new_name


book1 = Library("Rich dad poor dad")
book1.set_new_name("Hihi")
print(book1.get_name())






