# Write your solution here
from random import shuffle
def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as file:
        for line in file:
            word = line.strip()
            if word.startswith(beginning):
                word_list.append(word)
    shuffle(word_list)
    if n > len(word_list):
        raise ValueError
    else:
        return word_list[:n]




if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)