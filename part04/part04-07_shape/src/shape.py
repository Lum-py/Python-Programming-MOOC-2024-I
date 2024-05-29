# Copy here code of line function from previous exercise and use it in your solution
# Copy here code of line function from previous exercise
def line (integer: int, string: str):
    if string == "":
        print(integer * "*")   
    print(integer * string[0])

def shape(size: int, triangle: str, s_size: int, square: str):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(i, triangle)
        i += 1 
    for s in range(s_size):
        line(size, square)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")