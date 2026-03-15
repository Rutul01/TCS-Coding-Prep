n = int(input("Enter size of array: "))
arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

for i in arr:
    arr.sort()
print("Second Largest:", arr[-2])
print("Second Smallest: ", arr[1])