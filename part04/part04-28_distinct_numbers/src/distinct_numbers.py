# Write your solution here
def distinct_numbers(list: list):
    new = sorted(list)
    result = []
    for i in range(len(new)):
        if i == 0 or new[i] != new[i - 1]:
            result.append(new[i])
    return result


if __name__ == "__main__":
    my_list = [5, 6, 7, 8, 8, 9, 9, 5]
    print(distinct_numbers(my_list)) # [1, 2, 3]