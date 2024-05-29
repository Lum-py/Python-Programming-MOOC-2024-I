# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
i = word.find(char)

x = word[i:i + 3]

if len(x) >= 3:
    print(x)
