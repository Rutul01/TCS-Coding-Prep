arr = [1,2,2,2,2,2,2,3]

target = 2
low = 0
high = len(arr) - 1


firstoccurence = 0
lastoccurence = 0

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        firstoccurence = mid
        high = mid - 1
    elif arr[mid] < target:
        low = mid + 1
    else:
      high = mid - 1

    if arr[mid] == target:
        lastoccurence = mid
        low = mid + 1
    elif arr[mid] < target:
        high = mid - 1
    else:
      low = mid + 1
    
    