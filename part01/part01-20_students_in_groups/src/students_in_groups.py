# Write your solution here
students = int(input("How many students on the course? "))
size = int(input("Desired group size? "))
number = students // size
if students % size > 0:
    number += 1
    print(f"Number of groups formed: {number}")
else:
    print(f"Number of groups formed: {number}")