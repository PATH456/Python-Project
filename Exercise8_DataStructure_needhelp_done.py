#Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary.
#If not, delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {"John": 47, "Emma": 69, "Kelly": 76, "Jason": 97}

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {"John":47, "Emma":69, "Kelly":76, "Jason":97}
value = sample_dict.values()
list_value = list(value)
print(f"Value of sample_dict: {list_value} ")
for i in roll_number:
    if i in list_value:
        roll_number.remove(i)
    else:
        continue
print(f"After removing unwanted elements from list: {roll_number}")























