# Write your solution here
def invert(dictionary: dict):
    
    inverted_dict = {}
    for key in dictionary:
        inverted_dict[dictionary[key]] = key
    dictionary.clear()
    dictionary.update(inverted_dict)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)