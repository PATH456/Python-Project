sum = 0
next_num = 0

n = int(input('Enter a number here: '))
for i in range(n):
    next_num = next_num*10+2
    sum = sum + next_num
    print("next_num: ", next_num)

print("sum: ", sum)

















