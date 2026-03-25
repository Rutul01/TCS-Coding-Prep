#Reverse string using loops and inbuilt function
s = 'rutul'
rev = s[::-1]
print(rev)

a = 'rushi'
reverse_text = ''
for char in a:
    reverse_text = char + reverse_text
print(reverse_text)

#Reverse array using loop and inbuilt 
arr = [1,3,4,5,3,3,9]
i = 0
j = len(arr) - 1
while i < j:
    arr[i], arr[j] = arr[j],arr[i]
    i += 1
    j -= 1
print(arr)

#inbilt function
newarr = [1,3,4,5,3,3,9]
rev = newarr[::-1]
print(rev)


# Simple If else for calculating hours remeber if string is put what should we do 
n = input("Enter no of hours: ")
count = 0
if not n.isnumeric():
    print("Invalid input")
else:
    n = int(n)
    for i in range(1, n + 1):
        if i <= 2:
            count += 100
        elif i > 2 and i <= 5:
            count += 50
        else:
            count += 20
print(count)

# thsi question si regarding how many members you can put in car or age or simple hot air ballon question
n = int(input("Enter family members: "))
arr = []
k = int(input("Enter the maximum age: "))

for i in range(n):
    no = int(input(f"Enter the age of {i + 1} member: "))
    arr.append(no)
    
arr.sort()

totalmemb = 0
length = 0

for j in range(len(arr)):
    totalmemb += arr[j]

    if totalmemb <= k:
        length += 1
    else:
        break
print(length)

#this question is regarding how to calculate freq an highest freq in array and string 
arr = [1,1,2,2,2,3,3,3,3,3,4]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

maxfreq = 0
result = None
for key in freq:
    if freq[key] > maxfreq:
        maxfreq = freq[key]
        result = key
print(result)


s = 'absfsahaa'

strfreq = {}

for value in s:
    if value in strfreq:
        strfreq[value] += 1
    else:
        strfreq[value] = 1
print(strfreq)

strmaxfreq = 0
strresult = None
for key in strfreq:
    if strfreq[key] > strmaxfreq:
        strmaxfreq = strfreq[key]
        strresult = key

print(strresult)

# this is regarding calculte longest subarray with sum less than k 
arr = [4, 2, 2, 2, 2, 2, 2, 8, 1, 0] 
k = 8
longest = 0

for i in range(len(arr)):
    current_sum = 0

    for j in range(i,len(arr)):
        current_sum += arr[j]

        if current_sum > k:
            break
        length = j - i + 1
        longest = max(longest,length)   
print(longest)
    
    











