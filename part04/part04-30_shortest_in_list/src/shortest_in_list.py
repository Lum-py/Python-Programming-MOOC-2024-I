# Write your solution here
def shortest(list: list):
    word = list[0]
    for i in list:
        if len(i) < len(word):
            word = i
    return word

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)