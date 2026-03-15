s1 = input("Enter the word: ")
s2 = input("Enter the word: ")

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not A Anagram")