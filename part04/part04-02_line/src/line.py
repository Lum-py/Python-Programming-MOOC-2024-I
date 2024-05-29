# Write your solution here
def line (integer: int, string: str):
    if string == "":
        print(integer * "*")
    else:    
        print(integer * string[0])

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(10, "LOL")
    line(7, "%")
    line(5, "")