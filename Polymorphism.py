class Animal:
    def __init__(self, color):
        self.color = color


    def animal_sound(self):
        pass

class Cat(Animal):
    def animal_sound(self):
        return "Meow"

class Dog(Animal):
    def animal_sound(self):
        return "Bow"

cat = Cat("yellow")
dog = Dog("Yellow")

print(cat.animal_sound())
print(dog.animal_sound())




