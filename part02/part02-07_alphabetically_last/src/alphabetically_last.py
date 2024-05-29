# Write your solution here
w_1 = input("Please type in the 1st word: ")
w_2 = input("Please type in the 2nd word: ")
if w_1 > w_2:
    print(f"{w_1} comes alphabetically last.")
elif w_1 < w_2:
    print(f"{w_2} comes alphabetically last.")
else:
    print("You gave the same word twice.")