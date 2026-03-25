# Array sort without using any sort function plus or taking new array using two pointers
arr = [1,7,9,2,6,4]

for i in range(len(arr)):
    for j in range(i + 1,len(arr)):
        if arr[i] > arr[j]:
            arr[j], arr[i] = arr[i], arr[j]

print(arr)


# Two array merge it with sorted without using any function or sorting technique using two pointers
arr = [1,2,4,6,7,9]
arr1 = [1,2,3,7,8,9]    
newarr = []

arr = [1,2,4,6,7,9]
arr1 = [1,2,3,7,8,9]

i = 0
j = 0

while i < len(arr) and j < len(arr1):

    if arr[i] <= arr1[j]:
        newarr.append(arr[i])
        i += 1
    else:
        newarr.append(arr1[j])
        j += 1

while i < len(arr):
    newarr.append(arr[i])
    i += 1

while j < len(arr1):
    newarr.append(arr1[j])
    j += 1

print(newarr)