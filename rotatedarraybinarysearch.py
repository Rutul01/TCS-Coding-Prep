arr = [4,5,6,7,1,2,3]

target = 2

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print('Found', mid)
        break
    elif arr[low] <= mid and arr[low] <= target <= arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
    