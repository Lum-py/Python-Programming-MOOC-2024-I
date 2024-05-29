# Copy here code of line function from previous exercise
def line (integer: int, string: str):
    if string == "":
        print(integer * "*")
    else:    
        print(integer * string[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    i = size
    while i > 0:
        line(size, "#")
        i -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
