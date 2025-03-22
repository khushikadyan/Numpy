import numpy as np

def valid_step(board, row, col, num):
    """
    Check if placing `num` in `board[row, col]` is valid using NumPy operations.
    """
    # Check if the number is already in the row
    if np.any(board[row, :] == num):
        return False

    # Check if the number is already in the column
    if np.any(board[:, col] == num):  # Fixed: Use `:` for columns
        return False
    
    # Check if the number is in the 3x3 box
    start_row = 3 * (row // 3)  # Every first row of box is a multiple of 3 (0, 3, 6)
    start_col = 3 * (col // 3)  # Every first column of box is a multiple of 3 (0, 3, 6)
    if np.any(board[start_row:start_row+3, start_col:start_col+3] == num):
        return False
    
    return True

def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking and NumPy.
    """
    # Find the next empty cell (where value is 0)
    empty_cell = np.argwhere(board == 0)
    if len(empty_cell) == 0:
        return True  # No empty cells left, puzzle is solved
    
    row, col = empty_cell[0]  # Get the first empty cell
    
    for num in range(1, 10):
        if valid_step(board, row, col, num):  # Fixed: Changed `is_valid` to `valid_step`
            board[row, col] = num  # Place the number
            
            if solve_sudoku(board):  # Recursively solve the rest
                return True
            
            board[row, col] = 0  # Backtrack if the solution is invalid
    
    return False  # Trigger backtracking

def print_board(board):
    """
    Print the Sudoku board in a readable format using NumPy.
    """
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            print(board[row, col], end=" ")
        print()

# Example Sudoku board (0 represents empty cells)
sudoku_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

print("Original Sudoku Board:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("No solution exists")
# hence we solved the sudooko