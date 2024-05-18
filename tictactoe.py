import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (169, 169, 169)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

ROWS = 3
COLS = 3
SQUARE_SIZE = SCREEN_WIDTH // COLS


font = pygame.font.SysFont(None, 50)

board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]


symbols = {}


def draw_board():
    screen.fill(WHITE)
    for row in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (SCREEN_WIDTH, row * SQUARE_SIZE), 2)
    for col in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, SCREEN_HEIGHT), 2)


def draw_symbol(symbol, row, col):
    if symbol == 'X':
        text = font.render('X', True, RED)
    else:
        text = font.render('O', True, BLUE)
    screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE // 2 - text.get_width() // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2 - text.get_height() // 2))
    symbols[(row, col)] = text


def check_win(symbol):
    # Check rows and columns
    for i in range(ROWS):
        if all(board[i][j] == symbol for j in range(COLS)) or all(board[j][i] == symbol for j in range(ROWS)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(ROWS)) or all(board[i][COLS - 1 - i] == symbol for i in range(ROWS)):
        return True
    return False

# Function to check for a draw
def check_draw():
    return all(board[i][j] != ' ' for i in range(ROWS) for j in range(COLS))


def computer_turn():
    while True:
        row = random.randint(0, ROWS - 1)
        col = random.randint(0, COLS - 1)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            draw_symbol('O', row, col)
            break


def main():
    current_symbol = 'X'
    game_over = False

    while not game_over:
        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and current_symbol == 'X' and not game_over:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_row = mouse_y // SQUARE_SIZE
                clicked_col = mouse_x // SQUARE_SIZE
                if board[clicked_row][clicked_col] == ' ':
                    board[clicked_row][clicked_col] = current_symbol
                    draw_symbol(current_symbol, clicked_row, clicked_col)
                    if check_win(current_symbol):
                        print(f"Player {current_symbol} wins!")
                        game_over = True
                    elif check_draw():
                        print("It's a draw!")
                        game_over = True
                    else:
                        current_symbol = 'O'
            elif event.type == pygame.MOUSEBUTTONDOWN and current_symbol == 'O' and not game_over:
                computer_turn()  # Computer's turn
                if check_win('O'):
                    print("Computer wins!")
                    game_over = True
                elif check_draw():
                    print("It's a draw!")
                    game_over = True
                else:
                    current_symbol = 'X'


        for (row, col), symbol_text in symbols.items():
            screen.blit(symbol_text, (col * SQUARE_SIZE + SQUARE_SIZE // 2 - symbol_text.get_width() // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2 - symbol_text.get_height() // 2))

        pygame.display.flip()

if __name__ == "__main__":
    main()
