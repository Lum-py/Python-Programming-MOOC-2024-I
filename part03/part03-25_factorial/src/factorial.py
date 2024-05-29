# Write your solution here


while True:
    number = int(input("Please type a number: "))
    i = 1
    x = 1
    if number < 1:
        break
    while i <= number:
        x = x * i
        i += 1
    print(f"The factorial of the number {number} is {x}")
        


print("Thanks and bye!")   