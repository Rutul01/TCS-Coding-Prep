arr = [1,2,3,3,3,3,3]

target = 3

low = 0
high = len(arr) - 1
ans = -1

while low <= high:
    mid = ( low + high) // 2

    if arr[mid] == target:
        low = mid + 1
        ans = mid
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print(ans)