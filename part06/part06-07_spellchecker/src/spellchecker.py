# write your solution here
with open("wordlist.txt") as file:
    wordlist = file.read().split()
string = input("Write text: ")

words = string.split(" ")
    
for word in words:
    if not word.lower() in wordlist:
        word = "*" + word + "*"
    print(word, end= " ")