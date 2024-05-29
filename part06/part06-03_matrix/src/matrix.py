def read_matrix():
    matrix = []
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            row = []
            for number in numbers:
                row.append(int(number))
            matrix.append(row)
    return matrix
    

def matrix_sum():
    number = 0
    matrix = read_matrix()
    for line in matrix:
        for numbers in line:
            number += numbers
    return number
    
def matrix_max():
    number = 0
    matrix = read_matrix()
    for line in matrix:
        for numbers in line:
            if numbers > number:
                number = numbers
    return number
    

def row_sums():
    line_sum = []
    matrix = read_matrix()
    for line in matrix:
        line_sum.append(sum(line))
    return line_sum

if __name__ == "__main__":
    matrix_sum()
    matrix_max()
    row_sums()