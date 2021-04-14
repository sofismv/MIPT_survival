import pygame

WIDTH = 900
HEIGHT = 700
mazeSize = 20


class Wall(pygame.Rect):

    def __init__(self, x, y, width, height, horizon):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vertical = False
        self.horizontal = False

        if horizon:
            self.horizontal = True
            self.vertical = False
        else:
            self.horizontal = False
            self.vertical = True

        pygame.Rect.__init__(self, (x, y), (self.width, self.height))

    def draw_wall(self, screen, color):
        if self.vertical:
            pygame.draw.line(screen, color, [self.x, self.y], [self.x, self.height + self.y], 4)

        if self.horizontal:
            pygame.draw.line(screen, color, [self.x, self.y], [self.width + self.x, self.y], 4)

    def remove_wall(self):
        self.horizontal = False
        self.vertical = False

    def is_blocked(self, x, y, key_state):
        if key_state[pygame.K_RIGHT] and self.vertical:
            if x + WIDTH // mazeSize == self.x:
                return True
        elif key_state[pygame.K_LEFT] and self.vertical:
            if x == self.x:
                return True
        elif key_state[pygame.K_UP] and self.horizontal:
            if y == self.y:
                return True
        elif key_state[pygame.K_DOWN] and self.horizontal:
            if y + HEIGHT // mazeSize == self.y:
                return True
