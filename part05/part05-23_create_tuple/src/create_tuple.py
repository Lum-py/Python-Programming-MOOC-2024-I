# Write your solution here
def create_tuple(x: int, y: int, z: int):
    list = [x, y, z]
    smallest = min(list)
    largest = max(list)
    total = sum(list)
    new_tuple = (smallest, largest, total)
    return new_tuple

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))