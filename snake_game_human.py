
import pygame
from random import randrange

from snake import Snake, Body

#move to conf file pls
#CONSTANT
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220,20,60)

BODY_WIDTH = 15
BODY_HEIGHT = 15
SPACE_BETWEEN_PARTS = 1

GRID_SIZE = 480

SPEED = 16 # higher = faster
INITIAL_SNAKE_SIZE = 2

def new_game(render_ui=False):

    pygame.init()
    if render_ui:
        grid = pygame.display.set_mode([GRID_SIZE, GRID_SIZE])
        pygame.display.set_caption("ML learn snake")

    snake, cherry, delta_x, delta_y = init_game()
    clock = pygame.time.Clock()

    while snake.alive:
        cherry_eaten = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                snake.alive = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    delta_x, delta_y = go_left()
                if event.key == pygame.K_d:
                    delta_x, delta_y = go_right()
                if event.key == pygame.K_w:
                    delta_x, delta_y = go_up()
                if event.key == pygame.K_s:
                    delta_x, delta_y = go_down()

        if snake.body_parts[0].rect.colliderect(cherry):
            snake.sprite_list.remove(cherry)
            cherry_eaten = True

        snake.move(delta_x, delta_y, cherry_eaten)    

        # check colisions
        snake.alive = not(is_colisions(snake))

        # spawn cherry
        if cherry_eaten:
            cherry = Body(get_rand_in_grid(), get_rand_in_grid(), RED)
            # print(f"cherry {cherry}")
            snake.sprite_list.add(cherry)

        if render_ui:
            # clean screen:
            grid.fill(BLACK)

            #draw
            snake.sprite_list.draw(grid)

            # update screen
            pygame.display.flip()

        clock.tick(SPEED)

    print(f"END score: {snake.get_score()}")
    pygame.quit()

def is_colisions(snake: Snake):
    # fix colisions with wall
    def _colisions_with_wall():
        return snake.body_parts[0].rect.x <= 0 or snake.body_parts[0].rect.x >= GRID_SIZE-(BODY_WIDTH+SPACE_BETWEEN_PARTS) or snake.body_parts[0].rect.y <= 0 or snake.body_parts[0].rect.y >= GRID_SIZE-(BODY_WIDTH+SPACE_BETWEEN_PARTS)
    
    def _colisions_with_itself():
        head = snake.body_parts[0]
        # zero is head
        for parts in snake.body_parts[1:]:
            if parts.rect.colliderect(head):
                return True
        return False
    return _colisions_with_itself() or _colisions_with_wall()

def get_rand_in_grid():
    return randrange(1, GRID_SIZE/(BODY_WIDTH+SPACE_BETWEEN_PARTS), 1)*(BODY_WIDTH+SPACE_BETWEEN_PARTS)

def init_game():
    sprite_list = pygame.sprite.Group()
    snake = Snake(sprite_list, initial_size=INITIAL_SNAKE_SIZE)

    delta_x = BODY_WIDTH + SPACE_BETWEEN_PARTS
    delta_y = 0

    #initial cherry
    cherry = Body(get_rand_in_grid(), get_rand_in_grid(), RED)
    snake.sprite_list.add(cherry)

    return snake, cherry, delta_x, delta_y

def go_left():
    delta_x = (BODY_WIDTH + SPACE_BETWEEN_PARTS) * -1
    delta_y = 0
    return delta_x, delta_y

def go_right():
    delta_x = (BODY_WIDTH + SPACE_BETWEEN_PARTS) * 1
    delta_y = 0
    return delta_x, delta_y

def go_up():
    delta_x = 0
    delta_y = (BODY_WIDTH + SPACE_BETWEEN_PARTS) * -1
    return delta_x, delta_y

def go_down():
    delta_x = 0
    delta_y = (BODY_WIDTH + SPACE_BETWEEN_PARTS) * 1
    return delta_x, delta_y



def get_random_input():
    rand_number = randrange(0, 4, 1)
    if rand_number == 0:
        delta_x, delta_y = go_down()
    if rand_number == 1:
         delta_x, delta_y = go_left()
    if rand_number == 2:
         delta_x, delta_y = go_right()
    if rand_number == 3:
         delta_x, delta_y = go_up()
    return delta_x, delta_y


if __name__ == "__main__":

    #human game
    new_game(render_ui = True)

