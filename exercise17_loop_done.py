sum = 0
next_num = 0

n = int(input('Enter a number here: '))
for i in range(n):
    next_num = next_num*10+2
    sum = sum + next_num
    print("next_num: ", next_num)

print("sum: ", sum)

# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
result = 0
number = int(input("Enter a number here: "))
for i in range(1, number+1):
    sum = "2" * i
    result = result + int(sum)
print(result)

















