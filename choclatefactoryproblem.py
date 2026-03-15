n = 10
k = 3

for i in range(1,n+1):
    if n % i == 0 and i <= k:
        print("Divisors:",i)
