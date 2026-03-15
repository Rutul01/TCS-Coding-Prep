n = int(input("Enter the number: "))

originalnumber = n
digits = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** digits
    n = n // 10
if sum == originalnumber:
    print("Armstrongnumner")
else:
    print("Not a Armstrong")
