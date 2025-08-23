def validate_soduku(board):
    """
    Validate a Sudoku board.
    Args:
        board (list of list of int): A 9x9 Sudoku board represented as a list of lists.
    Returns:
        bool: True if the board is valid, False otherwise.
    """
    def is_valid_block(block):
        nums = [num for num in block if num != 0]
        return len(nums) == len(set(nums))

    # Check rows
    for row in board:
        if not is_valid_block(row):
            return False

    # Check columns
    for col in range(9):
        if not is_valid_block([board[row][col] for row in range(9)]):
            return False

    # Check 3x3 subgrids
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            block = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
            if not is_valid_block(block):
                return False

    return True

while True:
    user_input = input("Please enter a 9x9 Sudoku board (0 for empty cells, rows separated by commas): ")
    if not user_input:
        print("No input provided. Exiting the program.")
        break
    else:
        try:
            board = [[int(num) for num in row.split()] for row in user_input.split(',')]
            if len(board) != 9 or any(len(row) != 9 for row in board):
                print("Invalid board size. Please enter a valid 9x9 Sudoku board.")
                continue
            if validate_soduku(board):
                print("The Sudoku board is valid.")
            else:
                print("The Sudoku board is invalid.")
        except ValueError:
            print("Invalid input format. Please ensure you enter numbers only.")
        break

# write sample input for testing
# Example input: 2 9 5 7 4 3 8 6 1,4 3 1 8 6 5 9 2 7,8 7 6 1 9 2 5 4 3,3 8 7 4 5 9 2 1 6,6 1 2 3 8 7 4 9 5,5 4 9 2 1 6 7 3 8,7 6 3 5 2 4 1 8 9,9 2 8 6 7 1 3 5 4,1 5 4 9 3 8 6 7 2
# Example output: The Sudoku board is valid.