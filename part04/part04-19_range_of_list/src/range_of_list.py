# Write your solution here
def range_of_list(list):
    return max(list) - min(list)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print(result)