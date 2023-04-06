def find_empty(puzzle):
    # Find the next empty cell
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return (i, j)
    return None


def is_valid(puzzle, row, col, num):
    # Check row
    for i in range(9):
        if puzzle[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if puzzle[i][col] == num:
            return False

    # Check square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if puzzle[i][j] == num:
                return False

    return True


def solve(puzzle):
    # Find the next empty cell
    next_empty = find_empty(puzzle)
    if not next_empty:
        return True

    # Try all possible values for this cell
    row, col = next_empty
    for num in range(1, 10):
        if is_valid(puzzle, row, col, num):
            puzzle[row][col] = num

            # Recursively solve the puzzle
            if solve(puzzle):
                return True

            # If we're unable to solve the puzzle with this value, backtrack and try the next one
            puzzle[row][col] = 0

    # If no values work, the puzzle is unsolvable
    return False


puzzle = []
for i in range(9):
    row = input(f"Enter row {i+1} of the puzzle (use 0 for empty cells): ")
    puzzle.append([int(x) for x in row])

# puzzle = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

solve(puzzle)
for row in puzzle:
    print(row)
