from maze import Maze
import pygame
from pygame.locals import *
import sys

mainClock = pygame.time.Clock()

WHITE = (0, 0, 0)
BLACK = (229, 204, 255)


class Mini_game:

    def __init__(self, mazeSize, width, height, type_):
        self.type = type_
        self.mazeSize = mazeSize
        self.WIDTH = width
        self.HEIGHT = height

    def game_init(self, screen, all_sprites):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            screen.fill(BLACK)
            maze.draw_maze(screen, WHITE)
            all_sprites.draw(screen)
            all_sprites.update(maze)
            pygame.display.flip()

            pygame.display.update()
            mainClock.tick(60)
