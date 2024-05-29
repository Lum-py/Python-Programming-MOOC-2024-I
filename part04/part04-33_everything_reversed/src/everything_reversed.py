# Write your solution here
def everything_reversed(list: list):
    new = []
    for i in list:
        new.append(i[::-1])
    return new[::-1]
    

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)