# Write your solution here
number = int(input("Please type in a number: "))
small = "This number is smaller than 1000"
smaller = "This number is smaller than 100"
smallest = "This number is smaller than 10"
if number < 10:
    print(f"{small}\n{smaller}\n{smallest}")
elif number > 100 and number < 1000:
    print(small)
elif number > 10 and number < 1000:
    print(f"{small}\n{smaller}")

print("Thank you!")    