#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

given_number = str(input("Enter a number here: "))
index = -1
for i in given_number:
    print(given_number[index], end =" ")
    index = index - 1



































