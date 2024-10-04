l = [100, 200, 300, 400, 500, 600, 700, 800, 900]
key = 700
def find_number(list, target):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == key:
            return mid
        elif l[mid] < key:
            start = mid + 1
        elif l[mid] > key:
            end = mid - 1
        else:
            return -1

result = find_number(l, key)
if result != -1:
    print(f"The target number is at index {result}")
else:
    print("The target number is not found!")