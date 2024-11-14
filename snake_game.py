import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set the width and height of the screen (window size)
display_width = 800
display_height = 600

# Create the game window
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Clock to control the speed of the snake
clock = pygame.time.Clock()

# Snake block size
block_size = 20

# Font style and size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the player's score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    display.blit(value, [0, 0])

# Function to draw the snake
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], block_size, block_size])

# Function to display a message to the player
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width / 6, display_height / 3])

# The main function of the game
def gameLoop():  # Main loop
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = display_width / 2
    y1 = display_height / 2

    # Change in position
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1

    # Food position
    foodx = round(random.randrange(0, display_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, display_height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Check for boundaries
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, green, [foodx, foody, block_size, block_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(block_size, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # If the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, display_height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(15)

    pygame.quit()
    quit()


gameLoop()
