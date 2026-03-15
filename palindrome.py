n = int(input("Enter the palindrome number: "))

originalnumber = n
rev  = 0 

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if(rev == originalnumber):
    print("Palindrome")
else:
    print("Not a Palindrome")