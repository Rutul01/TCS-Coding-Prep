arr = [[2,3,1],
       [4,5,1],
       [5,6,9]]

#90 degree

for i in range(len(arr)):
    for j in range(i,len(arr)):
        arr[i], arr[j] = arr[j], arr[i]  # ====> transpose matrix

for i in range(len(arr)):
    arr[i].reverse()   # ====> rows chi aatli values reverse
print(arr)

#180 degree

arr.reverse()   # ====> purn rows ch swap karych asel tr
for i in range(len(arr)):
    arr[i].reverse()
print(arr)




