# Write your solution here
def same_chars(string, a: int, b: int):
    if 0 <= a < len(string) and 0 <= b < len(string):
        if string[a] == string[b]:
            return True
        else:
            return False
    else:
        return False    
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coders", 1, 2))