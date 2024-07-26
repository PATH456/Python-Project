#Exercise 4: Count the occurrence of each element from a list
#Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
for i in set(sample_list):
    count = sample_list.count(i)
    print("number from the list:", i, "Count:", count)











































