n = int(input("Enter the number: "))

addition = 0

originalnumber = n

def abudantnumber(n, addition):
    for i in range(1, n):
        if n % i == 0:
            addition += i
    if originalnumber < addition:
        print("Abudant number")
    else:
        print("Not Abudant number")

abudantnumber(n, addition)