# Write your solution here
def all_the_longest(list: list):
    new = []
    index = 0
    for l in list:
        if len(l) > index:
            index = len(l)
    for i in list:
        if len(i) == index:
            new.append(i)
    return new

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']