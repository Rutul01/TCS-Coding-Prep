arr = [1,4,5,2,5,6,8]

k = 5

longest = 0

for i in range(len(arr)):
    current_sum = 0

    for j in range(i, len(arr)):
        current_sum += arr[j]

        if current_sum <= k:
            length = j - i + 1
            max_sum = max(longest,length)
        else:
            break
print(max_sum)
