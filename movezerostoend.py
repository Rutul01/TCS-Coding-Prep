arr = [1,0,3,4,5,4,0,5,8,0,5]

for i in arr:
    if i == 0:
        arr.remove(i)
        arr.append(0)
print(arr)
