# Write your solution here
from difflib import get_close_matches

with open("wordlist.txt") as file:
    wordlist = file.read().split()
string = input("Write text: ")
sugestion = {}
for word in string.split(" "):
    if not word.lower() in wordlist:
        sugestion[word] = get_close_matches(word, wordlist)
        word = "*" + word + "*"
        
    print(word, end=" ")
print("\nsuggestions:")
for items in sugestion:
    print(f"{items}:", ', '.join(sugestion[items]))