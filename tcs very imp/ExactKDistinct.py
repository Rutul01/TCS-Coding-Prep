arr = [1,3,4,5,3,3,9]

i = 0
j = len(arr) - 1

while i < j:
    arr[i], arr[j] = arr[j],arr[i]
    i += 1
    j -= 1

print(arr)

newarr = [1,3,4,5,3,3,9]
rev = newarr[::-1]
print(rev)

s = 'rutul'
rev = s[::-1]
print(rev)

a = 'rushi'
reverse_text = ''
for char in a:
    reverse_text = char + reverse_text
print(reverse_text)