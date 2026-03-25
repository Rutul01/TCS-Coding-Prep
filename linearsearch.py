# find count the element 

arr = [1,2,3,4,4,2,4,6]

target = 4

count = 0

for i in arr:
    if i == target:
        count += 1
print(count)
