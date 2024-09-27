start = 25
end = 50
res_list = []
for i in range(start, end + 1):
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        res_list.append(i)


print(res_list)
 i = 27
 k = 2












