# Write your solution here
def add_entry():
    with open("diary.txt", "a") as file:
        new_line = input("Diary entry: ") 
        file.write(new_line +"\n")
        print("Diary saved")

def read_entry():
    with open("diary.txt") as file:
        for line in file:
            print(f"{line.strip()}")
            
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    key = input("Function: ")
    if key == "0":
        break
    elif key == "1":
        add_entry()
    elif key =="2":
        read_entry()

print("Bye now!")