res_list = []
index = 0
def addition(num1, num2):
    result = 0
    total = num1 + num2
    result += total
    res_list.append(result)
    return f"{num1} + {num2} = {total}"

def subtraction(num1, num2):
    result = 0
    subtract = num1 - num2
    result += subtract
    res_list.append(subtract)
    return f"{num1} - {num2} = {subtract}"

def multiplication(num1, num2):
    result = 0
    product = num1 * num2
    result += product
    res_list.append(product)
    return f"{num1} * {num2} = {product}"

def division(num1, num2):
    result = 0
    divide = num1 / num2
    result += divide
    res_list.append(divide)
    return f"{num1} / {num2} = {divide}"

num1 = int(input("What is the first number? "))
while True:
    operation = input("""Which operation that you choose? 
    +
    -
    *
    /
    """)
    num2 = int(input("What is the second number? "))
    if operation == "+":
        print(addition(num1, num2))
    elif operation == "-":
        print(subtraction(num1, num2))
    elif operation == "*":
        print(multiplication(num1, num2))
    elif operation == "/":
        print(division(num1, num2))
    else:
        print("Invalid operation!")
    user_choice = input("""Do you want to continue calculating or stop? 
    Type 'y' to continue or type 'n' to stop
    """)
    if user_choice == 'n':
        break
    elif user_choice == 'y':
        num1 = int(res_list[index])
        index += 1













#
# sample_dict = {
#     "+": calculation(20, 30)
#
# }
#
# result = sample_dict["+"]
# print(result)













