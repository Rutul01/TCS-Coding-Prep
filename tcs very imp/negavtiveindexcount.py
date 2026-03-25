n = int(input("Enter array size: "))
arr = list(map(int,input().split()))
k = 3

count = 0
newarr = []

for i in range(k):
    if arr[i] < 0:
        count += 1
newarr.append(count)

for i in range(k, len(arr)):
    if arr[i - k] < 0:
        count -= 1
    if arr[i] < 0:
        count += 1
    newarr.append(count)
print(newarr)