# Write your solution here
def print_square(layers, square_d):
    #iterate each row
    for i in range(2 * layers - 1):
        row = ""
        #iterate each column
        for j in range(2 * layers - 1):
            #calc distance from center
            distance = max(layers - i, layers - j, i - layers + 2, j - layers + 2)
            #append correct letter from dict
            row += square_d[distance]
        print(row)

layers = int(input("Layers: "))
square_d = {1: "A", 2: "B", 3: "C",4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 
          11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S",
           20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
print_square(layers, square_d)
