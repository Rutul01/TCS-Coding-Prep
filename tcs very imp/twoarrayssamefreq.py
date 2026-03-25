arr = [1,2,2,3]
arr1 = [1,2,3,2]

freq = {}
freq1 = {}

for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

for j in arr1:
    if j in freq1:
        freq1[j] += 1
    else:
        freq1[j] = 1
print(freq1)

if freq == freq1:
    print("Same Frequnecy")
else:
    print("No")