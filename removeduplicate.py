arr = list(map(int,input().split()))

for i in arr:
    if i not in arr:
        arr.remove(i)

print(arr)


# arr = list(map(int, input().split()))

# for i in range(len(arr)):
#     j = i + 1
#     while j < len(arr):
#         if arr[i] == arr[j]:
#             arr.pop(j)
#         else:
#             j += 1

# print(arr)

# [2,3,4,2]

# len(arr) = 4
# i = [0,1,2,3]
#  j = 0 + 1 = 1

# arr[i] = arr[j]
# 0 = 1  => 2 == 3  
# j = j + 1
# j = 2

# arr[i] = 1 +, index
#  arr[j] = 2
# 1 = 2> 3 == 4

#  j = 3
# arr[i] = 2+, index
# arr[j] = 3
# 2 =3> 4-== 2


