# Write your solution here
def length_of_longest(list: list):
    word = ""
    for i in list:
        if len(i) > len(word):
            word = i
    return len(word)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)