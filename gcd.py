n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(n1, n2) + 1):
    if n1 % i == 0 and n2 % i == 0:
        gcd = i

print("GCD:", gcd)

# formula : a, b == b, a % b

# while n2 > 0:
#    n1, n2 == n2, n1 % n2
#   print(n1)




