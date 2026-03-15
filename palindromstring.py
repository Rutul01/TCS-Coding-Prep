s = input("Enter the string: ")

originalstring = s
rev = ""

for i in s:
    rev = i + rev

if rev == originalstring:
    print("Palindrome")
else:
    print("Not a Palindrome")