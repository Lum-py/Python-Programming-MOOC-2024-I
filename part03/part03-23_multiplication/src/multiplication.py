# Write your solution here
number = int(input("Pease type in a number: "))
i = 1

while i <= number:
    x = 1
    while x <= number:

        print(f"{i} x {x} = {i * x}")
        x+= 1
    i += 1
