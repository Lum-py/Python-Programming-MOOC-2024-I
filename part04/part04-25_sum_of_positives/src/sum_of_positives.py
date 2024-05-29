# Write your solution here
def sum_of_positives(list):
    x = 0
    for i in list:
        if i > 0:
            x += i
    return x

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)