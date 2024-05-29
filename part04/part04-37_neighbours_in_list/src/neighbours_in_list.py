# Write your solution here
def longest_series_of_neighbours(list:list):
    count = 1
    longest = 1
    for i in range(1, len(list)):
        if abs(list[i - 1] - list[i]) == 1:
            count += 1
        else:
             count = 1
        longest = max(longest, count)
    return longest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))