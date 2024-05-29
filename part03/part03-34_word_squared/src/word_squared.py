# Write your solution here
def squared(string, amount):
    i = 0
    x = 0
    y = amount
    string *= amount
    #if amount % 2 != 0:
    string *= amount
    while i < amount:         
        print(string[x:y])
        i += 1      
        x += amount
        y += amount
    
if __name__ == "__main__":
    squared("ab", 3)