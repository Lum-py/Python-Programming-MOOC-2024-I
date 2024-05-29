# Write your solution here
def no_vowels(string: str):
    for char in string:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            string = string.replace(char, "")
    return string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))