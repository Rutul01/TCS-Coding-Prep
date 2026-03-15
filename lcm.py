n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

for i in range(max(n1, n2), n1 * n2 + 1):
    if i % n1 == 0 and i % n2 == 0:
        print("LCM:", i)
        break



# for example 12 and 18 =>
#     range(18,217) 
# 12 % 18 and 1* % 18 => 1,0 not valid 
# uptil the number it will go till both are divisible then break it like 36
# 12 and 18 both are diviisble then 0 and ans is 36


# using formula 
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))

# a = n1
# b = n2

# # Find GCD using Euclid's algorithm
# while b != 0:
#     a, b = b, a % b

# gcd = a

# lcm = (n1 * n2) // gcd

# print("LCM:", lcm)