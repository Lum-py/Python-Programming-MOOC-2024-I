# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word: str):
    return word == word[::-1]

while True:
    word = input("Please type in a palindrome: ")
    palindromes(word)
    if palindromes(word) == True:
        print(word, "is a palindrome!")
        break
    print("that wasn't a palindrome")