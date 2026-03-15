n = 100

arr = []


for i in range(1,n+1):
    length = len(str(i)) 
    temp = i
    num = 0
    while temp > 0:
        digit = temp % 10
        num = num + digit ** length
        temp = temp // 10
    if num == i:
        arr.append(i)
print(arr)
