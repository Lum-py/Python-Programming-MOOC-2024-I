# write your solution here
def read_fruits():
    with open("fruits.csv") as file:
        fruits = {}
        for i in file:
            fruit = i.split(";")
            fruits[fruit[0]] = float(fruit[1])
    return fruits 

if __name__ == "__main__":
    read_fruits()