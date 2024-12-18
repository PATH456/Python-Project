import string
import random

string_list = string.ascii_lowercase
string_total = 0

number_list = [0,1,2,3,4,5,6,7,8,9]
number_total = 0

symbol_list = ["!", "@","#","$","%","^","&","*"]
symbol_total = 0

password_list = []

choice_string = int(input("How many letters you want to have in your password? "))
choice_number = int(input("How many numbers you want to have in your password? "))
choice_symbol = int(input("How many symbols you want to have in your password? "))
for char in range (0, choice_string):
    str_random_index = random.randint(0, 24)
    password_list.append(string_list[str_random_index])


for num in range(0, choice_number):
    num_random_index = random.randint(0, 10)
    password_list.append(number_list[num_random_index])


for symbol in range(0, choice_symbol):
    sym_random_index = random.randint(0, 7)
    password_list.append(symbol_list[sym_random_index])

random.shuffle(password_list)

password_list = ''.join([str(item) for item in password_list])

print(f"Your password is: {password_list}")