s = input("Enter the word: ")

result = ""

for i in s:
    if i not in result :
        result = result + i
print(result)
