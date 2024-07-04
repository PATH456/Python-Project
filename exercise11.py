Exercise 10: Create a new list from two list using the following condition
Create a new list from two list using the following condition
Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
    
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list_result = []
for i in list1:
    if i % 2 == 1:
        list1_new = i
        print(f"Odd number in list1 is: {list1_new}")
        list_result.append(list1_new)
for y in list2:
    if y % 2 ==0:
        list2_new = y
        print(f"Even number in list2 is: {list2_new}")
        list_result.append(list2_new)
print(list_result)


































