#Exercise 5: Car Dealership

#Requirements:

    #Create a Car class with instance variables model, year, and price.
    #Add a class variable dealership_name representing the dealership's name.
    #Add another class variable total_cars_sold that tracks how many cars have been sold.
    #Add a method to mark a car as sold, and increment total_cars_sold each time a car is sold.
    #Print the dealership name and total number of cars sold after some cars are sold.
class Car:
    dealership_name = "Chuong Quoc Binh"
    total_cars_sold = 0

    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
        self.sold = False #the car hasn't been sold

    def sold_check(self):
        if self.sold == False:
            print(f"This {self.model} model is available for purchase, do you want to buy it?")
            choice = input().lower()
            if choice == "yes":
                Car.total_cars_sold += 1
                self.sold = True
                print(f"This {self.model} model has just been sold")
            else:
                print("Thank you for considering, we hope to see you later")
                pass
        else:
            print(f"Sorry, this {self.model} model has already been sold before, please choose another one")
car1 = Car("BMW", 2024, 80000)
car2 = Car("Porsche", 2022, 120000)
car3 = Car("Toyota", 2023, 50000)
print("Dealership's name:", Car.dealership_name)
car1.sold_check()
car2.sold_check()
print("Total sale:", Car.total_cars_sold)

car1.sold_check()














































    






















