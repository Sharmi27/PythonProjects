import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define constants
NUM_ROWS = 10
NUM_COLS = 10
SQUARE_SIZE = SCREEN_HEIGHT // NUM_ROWS

# Define snake and ladder heads and bottoms
snakes = {16: 6, 47: 26, 49: 11, 56: 43, 93: 71, 96: 78, 98: 73}
ladders = {4: 14, 9: 31, 21: 42,51: 63, 71: 91}

# Function to draw the board
def draw_board():
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 30)
    count = 1
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
            text = font.render(str(count), True, BLACK)
            screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE // 2 - text.get_width() // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2 - text.get_height() // 2))
            count += 1
    pygame.display.flip()

# Function to draw the player
def draw_player(position):
    row = (position - 1) // NUM_COLS
    col = (position - 1) % NUM_COLS
    pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 4)
    pygame.display.flip()

# Function to draw ladder and snake lines
def draw_lines():
    for start, end in ladders.items():
        start_row, start_col = (start - 1) // NUM_COLS, (start - 1) % NUM_COLS
        end_row, end_col = (end - 1) // NUM_COLS, (end - 1) % NUM_COLS
        pygame.draw.line(screen, GREEN, (start_col * SQUARE_SIZE + SQUARE_SIZE // 2, start_row * SQUARE_SIZE + SQUARE_SIZE // 2), (end_col * SQUARE_SIZE + SQUARE_SIZE // 2, end_row * SQUARE_SIZE + SQUARE_SIZE // 2), 3)
    for start, end in snakes.items():
        start_row, start_col = (start - 1) // NUM_COLS, (start - 1) % NUM_COLS
        end_row, end_col = (end - 1) // NUM_COLS, (end - 1) % NUM_COLS
        pygame.draw.line(screen, BLUE, (start_col * SQUARE_SIZE + SQUARE_SIZE // 2, start_row * SQUARE_SIZE + SQUARE_SIZE // 2), (end_col * SQUARE_SIZE + SQUARE_SIZE // 2, end_row * SQUARE_SIZE + SQUARE_SIZE // 2), 3)
    pygame.display.flip()

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to move the player
def move_player(current_position, dice_roll):
    new_position = current_position + dice_roll
    if new_position in snakes:
        print("Oops! You encountered a snake!")
        new_position = snakes[new_position]
    elif new_position in ladders:
        print("Congratulations! You climbed a ladder!")
        new_position = ladders[new_position]
    if new_position > 100:  # Correct if the new position exceeds 100
        new_position = 100
    return new_position

# Main game loop
def main():
    player_position = 1
    draw_board()
    draw_lines()
    draw_player(player_position)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dice_roll = roll_dice()
                    print("You rolled a", dice_roll)
                    if player_position != 100:  # Stop rolling dice if player reaches 100
                        new_position = move_player(player_position, dice_roll)
                        if new_position != player_position:
                            print("You moved to square", new_position)
                            draw_board()  # Clear the board
                            draw_lines()  # Draw lines again
                            draw_player(new_position)
                            player_position = new_position
                        if player_position == 100:
                            print("Congratulations! You won!")
                            running = False
                    else:
                        print("You already won! Game over.")
                        running = False

if __name__ == "__main__":
    main()