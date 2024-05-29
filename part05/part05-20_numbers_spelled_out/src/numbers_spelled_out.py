# Write your solution here
def dict_of_numbers():
    singles = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    dictionary = {}

    for number in range(100):
        if number < 10:
            dictionary[number] = singles[number]
        elif number < 20:
            dictionary[number] = teens[number]
        else:
            ten = number //10
            ones = number % 10
            if ones != 0:
                dictionary[number] = f"{tens[ten]}-{singles[ones]}"
            else:
                dictionary[number] = tens[ten]
    return dictionary



if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])