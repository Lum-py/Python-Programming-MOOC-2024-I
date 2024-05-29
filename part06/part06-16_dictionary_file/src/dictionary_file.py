# Write your solution here
def add_entry():
    with open("dictionary.txt", "a") as file:
        f_word = input("The word in finnish: ")
        e_word = input("The word in English: ") 
        file.write(f"{f_word};{e_word}\n")
        print("Dictionary entry added")

def search_entry():
    with open("dictionary.txt") as file:
        search_term = input("Search term: ")
        for search in file:
            search = search.split(";")
            if search_term in search[0] or search_term in search[1]:
                print(f"{search[0]} - {search[1]}", end="")
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    key = input("Function: ")
    if key == "3":
        break
    elif key == "1":
        add_entry()
    elif key =="2":
        search_entry()
    else:
        print("wrong input... try again")

print("Bye now!")
