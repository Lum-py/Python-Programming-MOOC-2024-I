# Write your solution here
n1 = int(input("number 1: "))
n2 = int(input("number 2: "))
operation = input("operation: ")
result = 0
if operation == "add":
    result = n1 + n2
    print(f"{n1} + {n2} = {result}")
if operation == "multiply":
    result = n1 * n2
    print(f"{n1} * {n2} = {result}")
if operation == "subtract":
    result = n1 - n2
    print(f"{n1} - {n2} = {result}")
