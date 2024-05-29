# Write your solution here
def first_word(string):
    string = string.split(" ")
    return string[0]        

def second_word(string):
    string = string.split(" ")
    return string[1]

def last_word(string):
    string = string.split(" ")
    return string[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))