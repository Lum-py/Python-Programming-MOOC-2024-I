# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
i = word.find(char)

while i < len(word):
    x = word[i:i+3]
    if len(x) >= 3:
        if x[0] == char:
            print(x)
    i = i + 1
