# Write your solution here
import string
def separate_characters(my_string: str):
    ascii_letters = string.ascii_letters
    ascii_punct = string.punctuation
    letters = ""
    punct = ""
    uml = ""
    for char in my_string:
        if char in ascii_letters:
            letters += char
        elif char in ascii_punct:
            punct += char
        else:
            uml += char
    return (letters, punct, uml)

if __name__ == "__main__":
    #separate_characters("Olé!!! Hey, are ümläüts wörking?")
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])