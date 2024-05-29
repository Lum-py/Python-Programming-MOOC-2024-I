# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()

    people = json.loads(data)
    for person in people:
        hobbies = ""
        for hobbie in person["hobbies"]:
            hobbies += f"{hobbie}, "
        print(f"{person["name"]} {person["age"]} years ({hobbies[0:-2]})")

if __name__ == "__main__":
    print_persons("file1.json")