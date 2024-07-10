#Exercise 9: Check Palindrome Number
#Write a program to check if the given number is a palindrome number.

#A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

numbers = input("Enter a number here: ")
if numbers[::-1] == numbers:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")






























