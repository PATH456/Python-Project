#Exercise 1: Animal Shelter

#Requirements:

    #Create an Animal class with instance variables species and age.
    #Add a class variable shelter_name that represents the shelter's name.
    #Add another class variable total_animals to keep track of how many animals have been taken in.
    #Create a method to print the total number of animals and the shelter name.

class Animal:
    shelter_name = "Heaven of Happiness"
    total_animals = 0
    def __init__(self, species, age):
        self.species = species
        self.age = age
        Animal.total_animals += 1

animal1 = Animal("sheep - livestock", 2)
animal2 = Animal("hen - poultry", 1)
animal3 = Animal("dog - livestock", 5)

print("Total number of animals:", Animal.total_animals)
print("Shelter's name:", Animal.shelter_name)








































    






















