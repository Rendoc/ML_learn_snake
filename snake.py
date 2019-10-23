import pygame

#CONSTANT #TODO put in config
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BODY_WIDTH = 15
BODY_HEIGHT = 15
SPACE_BETWEEN_PARTS = 1

GRID_SIZE = 480

class Body(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, color=WHITE):
        super().__init__()

        self.image = pygame.Surface([BODY_WIDTH, BODY_HEIGHT])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def __str__(self):
        return f"({self.rect.x}, {self.rect.y})"


class Snake:
    initial_pos_x = 240
    initial_pos_y = 240

    def __init__(self, sprite_list, initial_size, alive = True):
        self.body_parts = []
        self.sprite_list = sprite_list
        self.alive = alive
        self.initial_size = initial_size

        self._build_initial_snake()
    
    def _build_initial_snake(self):
        for i in range(self.initial_size):
            x = self.initial_pos_x - (BODY_WIDTH + SPACE_BETWEEN_PARTS) * i
            y = self.initial_pos_y

            body = Body(x, y)
            self.body_parts.append(body)
            self.sprite_list.add(body)


    def move(self, delta_x, delta_y, cherry):
        if not cherry:
            body_tail = self.body_parts.pop()
            self.sprite_list.remove(body_tail)

        head_pos_x = self.body_parts[0].rect.x + delta_x
        head_pos_y = self.body_parts[0].rect.y + delta_y

        head = Body(head_pos_x, head_pos_y)
        self.body_parts.insert(0, head)
        self.sprite_list.add(head)

        # print(self.body_parts[0])

