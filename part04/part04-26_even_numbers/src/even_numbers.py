# Write your solution here

def even_numbers(list: list):
    list_1 = []
    for i in list:
        if i % 2 == 0:
            list_1.append(i)
    return list_1

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
    