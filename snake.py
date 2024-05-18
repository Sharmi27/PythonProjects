import pygame
import random

# Initialize pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the snake and food sizes
BLOCK_SIZE = 20
SNAKE_SPEED = 10

# Set the font and font size
FONT = pygame.font.SysFont(None, 25)

# Set the directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


# Function to display text on the screen
def display_text(text, color, x, y):
    screen_text = FONT.render(text, True, color)
    game_display.blit(screen_text, [x, y])


# Function to draw the snake
def draw_snake(snake_list):
    for snake_block in snake_list:
        pygame.draw.rect(game_display, GREEN, [snake_block[0], snake_block[1], BLOCK_SIZE, BLOCK_SIZE])


# Function to display the score
def display_score(score):
    text = "Score: " + str(score)
    display_text(text, WHITE, 10, 10)


# Function to display game over message
def game_over():
    display_text("Game Over!", RED, SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 20)
    display_text("Press Q to Quit or C to Play Again", RED, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 20)
    pygame.display.update()


# Function to start the game
def start_game():
    snake_list = []
    snake_length = 1
    snake_speed = SNAKE_SPEED
    direction = RIGHT
    game_over_flag = False

    # Set initial position of the snake
    snake_head = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    snake_list.append(snake_head)

    # Set initial position of the food
    food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while not game_over_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    start_game()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != DOWN:
            direction = UP
        if keys[pygame.K_DOWN] and direction != UP:
            direction = DOWN
        if keys[pygame.K_LEFT] and direction != RIGHT:
            direction = LEFT
        if keys[pygame.K_RIGHT] and direction != LEFT:
            direction = RIGHT

        if direction == UP:
            snake_head[1] -= BLOCK_SIZE
        elif direction == DOWN:
            snake_head[1] += BLOCK_SIZE
        elif direction == LEFT:
            snake_head[0] -= BLOCK_SIZE
        elif direction == RIGHT:
            snake_head[0] += BLOCK_SIZE

        if snake_head[0] >= SCREEN_WIDTH or snake_head[0] < 0 or snake_head[1] >= SCREEN_HEIGHT or snake_head[1] < 0:
            game_over_flag = True

        snake_body = []
        snake_body.append(snake_head[0])
        snake_body.append(snake_head[1])
        snake_list.append(snake_body)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_over_flag = True

        if snake_head[0] == food_x and snake_head[1] == food_y:
            food_x = random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1

        game_display.fill(WHITE)
        pygame.draw.rect(game_display, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        draw_snake(snake_list)
        display_score(snake_length - 1)
        pygame.display.update()
        clock.tick(snake_speed)

    game_over()
    pygame.time.wait(3000)
    pygame.quit()
    quit()


# Set the game display
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set the game clock
clock = pygame.time.Clock()

# Start the game
start_game()
