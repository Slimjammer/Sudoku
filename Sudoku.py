import random

def is_safe_sudoku(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def fill_board(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                random_numbers = list(range(1, 10))
                random.shuffle(random_numbers)
                for num in random_numbers:
                    if is_safe_sudoku(board, row, col, num):
                        board[row][col] = num
                        if fill_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def remove_cells(board, num_cells_to_remove):
    cells_removed = 0
    while cells_removed < num_cells_to_remove:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            cells_removed += 1

def generate_sudoku(difficulty='medium'):
    board = [[0] * 9 for _ in range(9)]
    fill_board(board)

    if difficulty == 'easy':
        num_cells_to_remove = random.randint(30, 40)
    elif difficulty == 'medium':
        num_cells_to_remove = random.randint(40, 50)
    elif difficulty == 'hard':
        num_cells_to_remove = random.randint(50, 60)
    else:
        num_cells_to_remove = 45

    remove_cells(board, num_cells_to_remove)
    return board

def print_sudoku(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21) 
        row_display = ""
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_display += "| " 
            row_display += str(num) if num != 0 else "."
            row_display += " "
        print(row_display)

    print()

def solve_sudoku_util(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    row, col = empty_cell
    for num in range(1, 10):
        if is_safe_sudoku(board, row, col, num):
            board[row][col] = num
            if solve_sudoku_util(board):
                return True
            board[row][col] = 0
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board):
    solve_sudoku_util(board)
    print("Solved Sudoku:")
    print_sudoku(board)

def manual_solve(board):
    print("Enter your move in the format: row column number")
    print("Example: '1 2 3' places the number 3 in row 1, column 2.")
    print("Enter 'auto' at any time to let the code solve the puzzle.")
    
    while find_empty_cell(board):
        print_sudoku(board)
        move = input("Enter your move (or type 'auto' to solve): ").strip()
        
        if move.lower() == 'auto':
            solve_sudoku(board)
            return
        
        try:
            row, col, num = map(int, move.split())
            if board[row - 1][col - 1] == 0 and is_safe_sudoku(board, row - 1, col - 1, num):
                board[row - 1][col - 1] = num
            else:
                print("Invalid move. The cell is either filled or the number is not allowed. Try again.")
        except (ValueError, IndexError):
            print("Invalid input format. Please enter row, column, and number as integers (e.g., '1 2 3').")


def main_sudoku():
    difficulty = input("Choose difficulty level (easy, medium, hard): ").lower()
    board = generate_sudoku(difficulty)
    print("Generated Sudoku Puzzle:")
    print_sudoku(board)
    
    choice = input("Would you like to solve it yourself? (yes/no): ").strip().lower()
    if choice == 'yes':
        manual_solve(board)
    else:
        print("Auto-solving the puzzle:")
        solve_sudoku(board)

main_sudoku()
