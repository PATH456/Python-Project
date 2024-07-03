Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers
numbers = input('Enter a number here to check: ')
if numbers[0] == numbers[-1] and numbers[1] == numbers[-2] and numbers[2] == numbers[-3] and numbers[3] == numbers[-4]:
    print('Yes, it is a palindrome number')
else:
    print('No, it is not a palindrome number')































