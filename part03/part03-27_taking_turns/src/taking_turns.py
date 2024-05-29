# Write your solution here
number = int(input("Pease type in a number: "))
i = 1
while i+1 <= number:
    print(i)
    print(number)
    i += 1
    number -= 1
if i <= number:
    print(i)