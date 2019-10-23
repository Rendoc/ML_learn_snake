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

def main():

    pygame.init()

    # TODO ADD GRID OBJECT WITH SNAKE AND CHERRY AND SCREEN AREA
    grid = pygame.display.set_mode([GRID_SIZE, GRID_SIZE])
    pygame.display.set_caption("ML learn snake")

    sprite_list = pygame.sprite.Group()

    clock = pygame.time.Clock()
    
    snake = Snake(sprite_list, initial_size=2)

    delta_x = BODY_WIDTH + SPACE_BETWEEN_PARTS
    delta_y = 0

    #initial cherry
    cherry = Body(get_rand_in_grid(), get_rand_in_grid(), RED)
    snake.sprite_list.add(cherry)

    while snake.alive:
        cherry_eaten = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # you killed the snake by quitting
                snake.alive = False
            if event.type == pygame.KEYDOWN:
                # initial speed
                # print(event.key)
                if event.key == pygame.K_a:
                    delta_x = (BODY_WIDTH + SPACE_BETWEEN_PARTS) * -1
                    delta_y = 0
                if event.key == pygame.K_d:
                    delta_x = (BODY_WIDTH + SPACE_BETWEEN_PARTS) * 1
                    delta_y = 0
                if event.key == pygame.K_w:
                    delta_x = 0
                    delta_y = (BODY_WIDTH + SPACE_BETWEEN_PARTS) * -1
                if event.key == pygame.K_s:
                    delta_x = 0
                    delta_y = (BODY_WIDTH + SPACE_BETWEEN_PARTS) * 1

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
        # clean screen:
        grid.fill(BLACK)

        #draw
        snake.sprite_list.draw(grid)

        # turn on screen
        pygame.display.flip()

        clock.tick(10)
    print("END")
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
    
if __name__ == "__main__":
    main()