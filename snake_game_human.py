import pygame
from random import randrange

from snake import Snake, Body

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

    # pygame.init()

    # TODO ADD GRID OBJECT WITH SNAKE AND CHERRY AND SCREEN AREA

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

    delta_x = 0
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

class SnakeGame():

    def __init__(self, grid_size, render_ui = False):
        sprite_list = pygame.sprite.Group()
        self.snake = Snake(sprite_list, initial_size=INITIAL_SNAKE_SIZE)
        self.done = False
        self.board_dimensions = [grid_size, grid_size]
        self.render_ui = render_ui
        self.cherry = None

        self.cherry_eaten = False
    

    def start(self):
        self.spawn_cherry()
        if self.render_ui:
            self.init_render()
        return self.get_stats()
    

    def spawn_cherry(self):
        cherry = Body(get_rand_in_grid(), get_rand_in_grid(), RED)
        self.cherry = cherry
        self.snake.sprite_list.add(cherry)
        self.cherry_eaten = False
    

    def get_stats(self):
        return self.done, self.snake.get_score(), self.snake, self.cherry
    

    def init_render(self):
        self.grid = pygame.display.set_mode(self.board_dimensions)
        pygame.display.set_caption("ML learn snake")
        self.clock = pygame.time.Clock()

    

    def render(self):
        self.grid.fill(BLACK)
        #draw
        self.snake.sprite_list.draw(self.grid)
        # update screen
        pygame.display.flip()
        self.clock.tick(8)
    

    def end_game(self):
        print(f"END score: {self.snake.get_score()}")
        if self.render_ui:
            pygame.quit()
    

    def is_cherry_eaten(self):
        if self.snake.body_parts[0].rect.colliderect(self.cherry):
            self.snake.sprite_list.remove(self.cherry)
            self.cherry_eaten = True
        return self.cherry_eaten


    def get_vector_from_input(self, input):
        # 0:up
        # 1:right
        # 2:down
        # 3:left
        if input == 3:
            delta_x, delta_y = go_left()
        elif input == 1:
            delta_x, delta_y = go_right()
        elif input == 0:
            delta_x, delta_y = go_up()
        elif input == 2:
            delta_x, delta_y = go_down()
        
        return [delta_x, delta_y]
        
    def check_colisions(self):
        snake = self.snake
        def _colisions_with_wall():
            return snake.body_parts[0].rect.x <= 0 or snake.body_parts[0].rect.x >= GRID_SIZE-(BODY_WIDTH+SPACE_BETWEEN_PARTS) or snake.body_parts[0].rect.y <= 0 or snake.body_parts[0].rect.y >= GRID_SIZE-(BODY_WIDTH+SPACE_BETWEEN_PARTS)
        
        def _colisions_with_itself():
            head = snake.body_parts[0]
            # zero is head
            for parts in snake.body_parts[1:]:
                if parts.rect.colliderect(head):
                    return True
            return False
        if _colisions_with_itself() or _colisions_with_wall():
            self.snake.alive = False
            self.done = True

    def tick(self, input):
        vector = self.get_vector_from_input(input)
        if self.done:
            self.end_game()
        self.snake.move(vector[0], vector[1], self.is_cherry_eaten())    
        if self.is_cherry_eaten():
            self.spawn_cherry()
        
        self.check_colisions()
        if self.render_ui: 
            self.render()
        return self.get_stats()

if __name__ == "__main__":

    #human game
    new_game(render_ui = True)
