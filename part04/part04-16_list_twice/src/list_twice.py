# Write your solution here
list = []
s_list = []

while True:
    item = int(input("New item: "))
    if item == 0:
        break
    list.append(item)
    s_list = sorted(list)
    print("The list now:", list)
    print("The list in order:", s_list)

print("Bye!")