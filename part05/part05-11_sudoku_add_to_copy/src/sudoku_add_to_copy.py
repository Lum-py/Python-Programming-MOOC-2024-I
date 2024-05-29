# Write your solution here
def  print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(str(sudoku[i][j]) if sudoku[i][j] != 0 else '_', end=' ')
            
            # Add an extra space after every 3 items
            if (j + 1) % 3 == 0 and j < 8:
                print(' ', end='')
        print()        
        # Add a newline after every 3 rows
        if (i + 1) % 3 == 0 and i < 8:
            print()
    

    

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
     grid_copy = [row[:] for row in sudoku]
     
     grid_copy[row_no][column_no] = number

     return grid_copy

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)