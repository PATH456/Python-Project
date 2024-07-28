#Exercise 6: Create a recursive function
#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
#A recursive function is a function that calls itself again and again.

n = int(input())
sum = 0
def total(n, sum):
    sum = sum + n
    cal = n -1
    if n-1 == 0:
        return sum
    else:
        return total(cal, sum)

result = total(n, sum)
print(result)











