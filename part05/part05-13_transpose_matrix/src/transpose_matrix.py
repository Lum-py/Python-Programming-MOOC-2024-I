# Write your solution here
def transpose(matrix: list):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j],  matrix[j][i] = matrix[j][i], matrix[i][j]

    # Print the modified matrix (now transposed)
    print(matrix)

if __name__ == "__main__":
    matrix = [[1, 2],[1, 2],]
    transpose(matrix)