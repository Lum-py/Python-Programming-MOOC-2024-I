# Write your solution here
print("Person 1:")
p_1 = input("Name: ")
a_1 = int(input("Age: "))
print("Person 2:")
p_2 = input("Name: ")
a_2 = int(input("Age: "))

if a_1 > a_2:
    print(f"The elder is {p_1}")
elif a_1 < a_2:
    print(f"The elder is {p_2}")
else:
    print(f"{p_1} and {p_2} are the same age")       