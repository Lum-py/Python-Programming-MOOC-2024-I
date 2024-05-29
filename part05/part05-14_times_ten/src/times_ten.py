# Write your solution here
def times_ten(start_intex: int, end_index: int):
    dictionary = {}
    for i in range(start_intex, end_index + 1):
        dictionary[i] = i * 10
    return dictionary

if __name__ == "__main__":
    d = times_ten(3, 6)

    print(d)