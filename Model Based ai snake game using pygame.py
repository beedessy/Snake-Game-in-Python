

from tkinter.constants import CURRENT, FALSE, TRUE
import pygame, sys, time, random


snake_speed = 10

# Window size
window_x = 600
window_y = 600

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

# Initialise game window
pygame.display.set_caption('Snake Game By Lucshika Beedessy')
game_window = pygame.display.set_mode((window_x, window_y))

# Colors (R, G, B)
coral = pygame.Color(228, 204, 223)
red = pygame.Color(106, 5, 5)
black = pygame.Color(5, 5, 5)
pink = pygame.Color(255, 0, 200)
blue = pygame.Color(0, 0, 255)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

# Game variables
snake_position = [window_x / 2, window_y / 2]
snake_body = [[window_x / 2, window_y / 2], [(window_x / 2) - 10, window_y / 2],
              [(window_x / 2) - (2 * 10), window_y / 2]]

fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

direction = 'RIGHT'
changeDirection = direction

score = 0


# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED MAN', True, black)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.fill(coral)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, black, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (window_x / 10, 15)
    else:
        score_rect.midtop = (window_x / 2, window_y / 1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()


# SNAKE AUTOMATION MODEL BASED AGENT

def rule_match():
    # last direction it moved in
    global new_direction, state, current_head_x, current_head_y

    # get state from direction and position
    state = direction
    current_head_x = snake_position[0]
    current_head_y = snake_position[1]

    # Rules

    # get a random direction to move in
    new_direction = get_Random_Direction()

    # Check if hit with wall or tail
    if (check_hit_with_wall(new_direction, current_head_x, current_head_y) == True) or (
            hit_body(new_direction, current_head_x, current_head_y) == True):

        while (check_hit_with_wall(new_direction, current_head_x, current_head_y) == True) or (
                hit_body(new_direction, current_head_x, current_head_y) == True):
            new_direction = get_Random_Direction()
            if (check_hit_with_wall(new_direction, current_head_x, current_head_y) == False and hit_body(new_direction,
                                                                                                         current_head_x,
                                                                                                         current_head_y) == False):
                return new_direction
                # state=action
                break
            continue

    elif (check_hit_with_wall(new_direction, current_head_x, current_head_y) == False and hit_body(new_direction,
                                                                                                   current_head_x,
                                                                                                   current_head_y) == False):
        return new_direction
        # state=action


def get_Random_Direction():
    global curr_direction
    curr_direction = direction
    # Generate direction to get direction
    num = random.randrange(0, 4)

    if (num == 0) and direction != 'DOWN':
        curr_direction = 'UP'
    elif (num == 1) and direction != 'UP':
        curr_direction = 'DOWN'
    elif (num == 2) and direction != 'RIGHT':
        curr_direction = 'LEFT'
    elif (num == 3) and direction != 'LEFT':
        curr_direction = 'RIGHT'

    return curr_direction


def hit_body(new_direction, x, y):
    flag1 = False
    for body_part in snake_body[1:]:
        if x + 10 == body_part[0] and y == body_part[1] and new_direction == 'RIGHT':
            flag1 = True
        elif x - 10 == body_part[0] and y == body_part[1] and new_direction == 'LEFT':
            flag1 = True
        elif x == body_part[0] and y + 10 == body_part[1] and new_direction == 'DOWN':
            flag1 = True
        elif x == body_part[0] and y - 10 == body_part[1] and new_direction == 'UP':
            flag1 = True
    return flag1


def check_hit_with_wall(new_direction, x, y):
    global flag
    flag = False

    if new_direction == 'UP' and (y - 10 < 0):
        flag = True
    elif new_direction == 'DOWN' and (y + 10 > window_y - 10):
        flag = True
    elif new_direction == 'LEFT' and (x - 10 < 0):
        flag = True
    elif new_direction == 'RIGHT' and (x + 10 > window_x - 10):
        flag = True
    return flag


def rule_action():
    global action, state
    action = rule_match()
    state = action
    return action


# def timer():
#     period= random.randrange(1,5)
#     return period

# time_tick=pygame.time.get_ticks()
# Main logic
while True:

    # secs=(pygame.time.get_ticks()-time_tick)/1000
    # if secs>10:
    #     game_over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    changeDirection = rule_action()

    # print(direction)
    # direction=modelBasedReflexAgent()
    # change_to=direction
    # move_in_direction=timer()
    # print(direction)
    # print(move_in_direction)
    # while move_in_direction!=0:
    #   change_to=direction

    #   move_in_direction-=1

    # Making sure the snake cannot move in the opposite direction instantaneously
    if changeDirection == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if changeDirection == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if changeDirection == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if changeDirection == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not fruit_spawn:
        # make sure food does not spawn on the snake
        food_detected = True
        while food_detected:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
            food_detected = False

            for body_part in snake_body[:]:
                if (fruit_position[0] == body_part[0] and snake_position[1] == body_part[1]):
                    food_detected = True

    fruit_spawn = True

    # GFX
    game_window.fill(coral)
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, pink, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    # timer for death

    show_score(1, red, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    fps_controller.tick(snake_speed)