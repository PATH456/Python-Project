#Exercise 4: Count the occurrence of each element from a list
#Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
result = dict()
count = 1
for i in sample_list:
    if i not in result:
        result[i] = count
    else:
        result[i] += 1
print(result)











































