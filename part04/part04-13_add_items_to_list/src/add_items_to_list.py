# Write your solution here
items = int(input("How many items: "))
my_list = []

while len(my_list) < items:
    my_list.append(int(input(f"Item {len(my_list) + 1}: ")))

print(my_list)