# Write your solution here
def print_sudoku(sudoku: list):
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

    '''
   for row in sudoku:
        for element in row:
            print(str(element) if element != 0 else '_', end=' ')
        print()
    '''
def add_number(sudoku:list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
          

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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)