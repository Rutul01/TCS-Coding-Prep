arr = [4, 2, 2, 2, 2, 2, 2, 8, 1, 0] 
k = 8
longest = 0

for i in range(len(arr)):
    current_sum = 0

    for j in range(i,len(arr)):
        current_sum += arr[j]

        if current_sum > k:
            break
        length = j - i + 1
        longest = max(longest,length)   
print(longest)