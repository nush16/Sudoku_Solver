import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set up the Pygame window
pygame.init()
size = (540, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sudoku Solver")

# Create the Sudoku board
board = [[0] * 9 for _ in range(9)]

# Define some helper functions
def draw_board():
    """Draws the Sudoku board on the Pygame screen"""
    screen.fill(WHITE)
    
    # Draw the 3x3 sub-grid
    pygame.draw.rect(screen, BLACK, [60, 60, 540, 540], 2)
    for i in range(0, 10, 3):
        for j in range(-1, 10, 3):
            pygame.draw.rect(screen, BLACK, [j * 60 + 60, i * 60 + 60, 180, 180], 2)

    # Draw the cell borders and numbers
    for i in range(9):
        for j in range(9):
            x = j * 60
            y = i * 60 + 60
            pygame.draw.rect(screen, GRAY, [x, y, 60, 60], 1)
            if board[i][j] != 0:
                font = pygame.font.SysFont('calibri', 50)
                text = font.render(str(board[i][j]), True, BLACK)
                screen.blit(text, (x + 20, y + 5))
def solve():
    """Solves the Sudoku puzzle using a backtracking algorithm"""
    # Find the next empty cell
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    # Try each possible value
                    if is_valid(i, j, n):
                        board[i][j] = n
                        draw_board()
                        pygame.display.update()
                        pygame.time.delay(100)
                        if solve():
                            return True
                        board[i][j] = 0
                return False
    return True

def is_valid(row, col, num):
    """Checks if a number can be placed in a certain position"""
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

# Main game loop
selected = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Set the selected cell to the one that was clicked on
                pos = pygame.mouse.get_pos()
                col = pos[0] // 60
                row = (pos[1] - 60) // 60
                selected = (row, col)
            elif event.button == 3:
                selected = None
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isdigit():
                if selected:
                    # Update the board with the new value
                    row, col = selected
                    board[row][col] = int(event.unicode)
            elif event.key == pygame.K_BACKSPACE:
                if selected:
                    row, col = selected
                    board[row][col] = 0
            elif event.key == pygame.K_RETURN:
                solve()

    draw_board()
    pygame.display.update()

pygame.quit()
