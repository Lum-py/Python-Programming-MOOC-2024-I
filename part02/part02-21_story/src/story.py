# Write your solution here
story = ""
word_1 = ""
while True:
    word = input("Please type in a word: ")    
    if word == word_1 or word == "end":
        break
    story += word + " "
    word_1 = word
print(story)