# Write your solution here

def filter_incorrect():
    with open("correct_numbers.csv", "w") as new_file:
        with open("lottery_numbers.csv") as file:
            for line in file:
                part = line.strip().split(";")
                week = part[0].split(" ")
                numbers = []
                for number in part[1].split(","):
                    if number.isdigit():
                        number = int(number)
                        if number > 0 and number < 40 and not number in numbers:
                            numbers.append(number)
                if not week[1].isdigit() or len(numbers) != 7:
                    continue 
                               
                new_file.write(line)

if __name__ == "__main__":
    filter_incorrect()
