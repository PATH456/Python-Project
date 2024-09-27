from abc import ABC, abstractmethod

class Animal(ABC):  # Inherits from ABC
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bow"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Create instances of Dog and Cat
dog = Dog("Chovy")
cat = Cat("Lehends")
print(dog.sound())  # Output: Bow
print(cat.sound())  # Output: Meow






