# n = int(input("Enter array size: "))
# arr = []

# for i in range(n):
#     arr.append(int(input(f"Enter the element {i + 1}: "))) 
# arr = [1,1,2,2,2,3,3,3,3,3,4]

# freq = {}

# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# maxfreq = 0
# result = None
# for key in freq:
#     if freq[key] > maxfreq:
#         maxfreq = freq[key]
#         result = key
# print(result)















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