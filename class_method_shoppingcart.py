 #Write a Python program to create a class representing a shopping cart.
 #Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    supermarket_name = "Go!"

    def __init__(self, items = None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def add_item(self, item, price):
        item_add = (item, price)
        if item_add not in self.items:
            self.items.append(item_add)

    def remove_item(self, item, price):
        item_remove = (item, price)
        self.items.remove(item_remove)



cart1 = ShoppingCart()

cart1.add_item("Watermelon", 30)
cart1.add_item("Papaya", 20)
sample_list = []
for i in cart1.items:
    sample_list.append(i[1])
print(sum(sample_list))











































































































    






















