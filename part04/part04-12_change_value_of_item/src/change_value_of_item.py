# Write your solution here
my_list = [1, 2, 3, 4, 5]
while True:
    i = int(input("Index: "))
    if i == -1:
        break
    my_list[i] = int(input("New value: "))
    print(my_list)
