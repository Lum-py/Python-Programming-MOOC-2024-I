# Write your solution here
def spruce(size):
    print("a spruce!")
    x = size - 1
    
    string = "*"
    while x >= 0:
        space = " " * x
        print(space + string)
        x -= 1
        string += "**" 
    print(" " * (size - 1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)