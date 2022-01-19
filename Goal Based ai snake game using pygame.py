import pygame
import time
import random

from pygame import QUIT, KEYDOWN, K_ESCAPE

snake_speed = 25

# Window size
window_x = 600
window_y = 600

# defining colors
coral = pygame.Color(228, 204, 223)
red = pygame.Color(106, 5, 5)
black = pygame.Color(5, 5, 5)
pink = pygame.Color(255, 0, 200)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game By Lucshika Beedessy')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'right'
#changeDirection is for what will next direction snake and to take
changeDirection = direction
#dirout variable is uses when fruit position is in wrong side and snake must turn
dirout='right'

#global flag is use when fruit is in wrong side and snake have to turn to go in specific location
global flag
flag=True

# initial score
score = 0


# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # displaying text
    game_window.blit(score_surface, score_rect)


# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 35)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Game Over,Your Score is : ' + str(score), True, black)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 5 seconds we will quit the program
    time.sleep(5)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


#  Model based functions
# determine state
# function called when fruit position out of accessible location by rules function
def checkdir():
    global flag
    global dirout
    if changeDirection == 'right':
        if snake_position[0] > fruit_position[0]:
            print("in checkdir if right")
            flag = False
            dirout = 'down'
            print("log in checkdir :" + dirout)

    if changeDirection == 'left':
        if snake_position[0] < fruit_position[0]:
            print("in checkdir if left")
            flag = False
            dirout = 'up'
            print("log in checkdir :" + dirout)

    if changeDirection == 'up':
        if snake_position[1] < fruit_position[1]:
            print("in cheakdir if up")
            flag = False
            dirout = 'right'
            print("log in checkdir :" + dirout)

    if changeDirection == 'down':
        if snake_position[1] > fruit_position[1]:
            print("in checkdir if down")
            flag = False
            dirout = 'left'
            print("log in checkdir :" + dirout)

# function always called when snake is in direction where fruit position can be match
#rule match
# this function is take status of current direction and make decision of next direction
def  rules():

    if direction == 'right':
        if snake_position[0] == fruit_position[0]:
            if snake_position[1] < fruit_position[1]:
                return 'down'
            else:
                return 'up'
        else:
            return 'right'
    if direction == 'left':
        if snake_position[0] == fruit_position[0]:
            if snake_position[1] < fruit_position[1]:
                return 'down'
            else:
                return 'up'
        else:
            return 'left'
    if direction == 'up':
        if snake_position[1] == fruit_position[1]:
            if snake_position[0] < fruit_position[0]:
                return 'right'
            else:
                return 'left'
        else:
            return 'up'
    if direction == 'down':
        if snake_position[1] == fruit_position[1]:
            if snake_position[0] < fruit_position[0]:
                return 'right'
            else:
                return 'left'
        else:
            return 'down'



# Main Function
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_UP:
                changeDirection = 'up'
            if event.key == pygame.K_DOWN:
                changeDirection = 'down'
            if event.key == pygame.K_LEFT:
                changeDirection = 'left'
            if event.key == pygame.K_RIGHT:
                changeDirection = 'right'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

   ##If two keys pressed simultaneously we don't want snake to move into two directions simultaneously
   #  if changeDirection == 'up' and direction != 'down':
   #      direction = 'up'
   #  if changeDirection == 'down' and direction != 'up':
   #      direction = 'down'
   #  if changeDirection == 'left' and direction != 'right':
   #      direction = 'left'
   #  if changeDirection == 'right' and direction != 'left':
   #      direction = 'right'


   #  # Moving the snake
   #  if direction == 'up':
   #      snake_position[1] -= 10
   #  if direction == 'down':
   #      snake_position[1] += 10
   #  if direction == 'left':
   #      snake_position[0] -= 10
   #  if direction == 'right':
   #      snake_position[0] += 10




   #take action
    # flag initially true for checking snake will have fruit position accessible or not
    flag = True
    # print the state of the directon
    print("current direction :" + changeDirection)

    # call checkdir() function to check fruit position is accessible or not
    checkdir()
    changeDirection = dirout
    print("log checkdir after :" + dirout)
    # if flag still true than call second function to do regular things
    if (flag == True):
        changeDirection = rules()
        print("log if flag TRUE :" + dirout)

   #return action and move the snake
    # following few lines checking that input is reverse direction to current input than block can not take input
    # issue:if out rules() function  continue input of same direction than might snake will crash into itself
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection
    if direction == 'right':
        snake_position[0] += 10
    if direction == 'left':
        snake_position[0] -= 10
    if direction == 'up':
        snake_position[1] -= 10
    if direction == 'down':
        snake_position[1] += 10







    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(coral)

    for pos in snake_body:
        pygame.draw.rect(game_window, pink,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        changeDirection = rules()
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        changeDirection = rules()
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            changeDirection = rules()
            game_over()

    # displaying score continuously
    show_score(1, red, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)