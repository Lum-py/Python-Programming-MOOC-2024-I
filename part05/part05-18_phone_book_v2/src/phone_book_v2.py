# Write your solution here
phonebook = {}

while True:
    usr_input = input("command (1 search, 2 add, 3 quit): ")

    if usr_input == "1":
        search = input("name: ")
        if search in phonebook:
            for number in phonebook[search]:
                print(number)
        else:
            print("no number")

    elif usr_input == "2":
        name = input("name: ")
        if name not in phonebook:
            phonebook[name] = [input("number: ")]
        else:
            phonebook[name].append(input("number: "))
        print("ok!")

    elif usr_input == "3":
        break
    
print("quitting...")