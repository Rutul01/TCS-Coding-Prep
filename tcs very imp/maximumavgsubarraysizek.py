n = int(input("Enter the array size: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter elements {i + 1}: ")))
print(arr)
k = 3
arrsumfirst = sum(arr[:k])
maxsum = arrsumfirst / k

for i in range(k, len(arr)):
    arrsumfirst = arrsumfirst + arr[i]
    arrsumfirst = arrsumfirst - arr[i - k]

    if arrsumfirst / k > maxsum:
        maxsum = arrsumfirst / k
    
print(maxsum)
    


   


    
