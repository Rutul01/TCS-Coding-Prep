arr = [1,2,2,3,4]
target = 2
low = 0
high = len(arr) - 1
ans = -1  #by default

while low <= high:
    mid = (low + high)//2

    if arr[mid] == target:
        ans = mid
        high = mid - 1
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print(ans)
