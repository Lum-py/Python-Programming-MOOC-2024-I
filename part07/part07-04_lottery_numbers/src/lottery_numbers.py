# Write your solution here
def lottery_numbers(amount: int, lower: int, upper: int):
    # from random import randint
    # numbers = []
    # while len(numbers) < amount:
    #     new_number = randint(lower, upper)
    #     if new_number not in numbers:
    #         numbers.append(new_number)
    # return sorted(numbers)
    from random import shuffle
    numbers = list(range(lower, upper))
    shuffle(numbers)
    draw = numbers[0:amount]
    return sorted(draw)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)