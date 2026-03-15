s = input("Enter the string: ")

vowels = 0
consonnats = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': 
        vowels = vowels + 1
    else:
        consonnats = consonnats + 1
print("Voewls: ", vowels)
print("Consonants: ", consonnats)
