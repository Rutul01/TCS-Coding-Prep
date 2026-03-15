s = input("Enter the sentence: ")

count = 1

for i in s:
    if i == " ":
        count = count + 1
print(count)
