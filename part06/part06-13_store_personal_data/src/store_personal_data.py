def store_personal_data(person:tuple):
    with open("people.csv", "a") as file:
        file.write(f"{person[0]};{person[1]};{person[2]}")


if __name__ == "__main__":
    person = ("Paul Paulson", 37, 175.5)
    store_personal_data(person)


# Write your solution here