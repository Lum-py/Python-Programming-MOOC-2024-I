# Write your solution here
list = []
while True:
    print(f"The list is now {list}")
    choice = input("a(d)d, (r)emove or e(x)it: ").lower()
    if choice == "x":
        break
    elif choice == "d":
        list.append(len(list) + 1)        
    elif choice == "r":
        list.remove(len(list))        

print("Bye!")