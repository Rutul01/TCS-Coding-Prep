s = input("Enter sentence: ")

words = s.split()

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i
print(longest)
