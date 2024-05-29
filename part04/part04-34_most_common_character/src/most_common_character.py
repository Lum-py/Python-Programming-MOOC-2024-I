# Write your solution here
def most_common_character(string: str):
    most_common = ""
    count = 0
    for i in string:
        if string.count(i) > count:
            count = string.count(i)
            most_common = i 
    return most_common   

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))