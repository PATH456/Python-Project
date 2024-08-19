#Exercise 5: Remove items from the set at once

#Write a Python program to remove items 10, 20, 30 from the following set at once.

#Given:

set1 = {10, 20, 30, 40, 50}

#Expected output:

{40, 50}
set2 = set()
for i in set1:
    if i > 30:
        set2.add(i)
    else:
        pass
print(set2)
#dont know how to remove an items in a set properly



