l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 60
start = 0
end = len(l) - 1
def find_number(start, end):
    mid = (start + end) // 2
    if l[mid] == target:
        return mid
    elif l[mid] < target:
        return find_number(mid +1, end)
    elif l[mid] > target:
        return find_number(start, mid -1)
    else:
        return False
result = find_number(start, end)
if result != False:
    print(f"This number is in {result} index")
else:
    print("This number is not found")
