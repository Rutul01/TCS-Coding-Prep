n = int(input("Enter the number: "))

originalnumber = n

arr = []

for i in range(1, n):
    if n % i == 0:
        arr.append(i)

addition = sum(arr)

if originalnumber == addition:
    print("Perfect Number", addition)
else:
    print("Not a Perfect Number", addition)

# Optimized code

#for i in range(1, n):
#    if n % i == 0:
#        sum_div += i