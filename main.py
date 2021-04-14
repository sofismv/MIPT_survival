import random
from tile import Tile
import pygame
import os
from maze import Maze

WIDTH = 480
HEIGHT = 600
FPS = 60
mazeSize = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 120)

tileWidth = WIDTH // mazeSize

while tileWidth % 2 != 0:
    tileWidth += 1

if tileWidth * mazeSize > WIDTH:
    tileWidth -= 1
    while tileWidth % 2 != 0:
        tileWidth -= 1

tileHeight = HEIGHT // mazeSize

while tileHeight % 2 != 0:
    tileHeight += 1

if tileHeight * mazeSize > HEIGHT:
    tileHeight -= 1
    while tileHeight % 2 != 0:
        tileHeight -= 1

WIDTH = tileWidth * mazeSize
HEIGHT = tileHeight * mazeSize

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MIPT_survival!")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

maze = Maze(mazeSize, WIDTH, HEIGHT)


class Student(pygame.sprite.Sprite):

    survivor_img = pygame.image.load('/Users/sofiasamoylova/Desktop/MIPT survival/MIPT-survival/img/pac.png')
    live_goal = "none"
    socialization_level = 5
    mark = 5
    health = 3
    pleasure = 5
    scholarship = 1

    def __init__(self, goal):
        pygame.sprite.Sprite.__init__(self)
        self.original_img = Student.survivor_img
        self._socialization_goal_ = goal
        self.original_img = pygame.transform.scale(self.original_img, (Tile.widthTile,Tile.heightTile))
        self.rect = self.original_img.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8

        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT:
            self.rect.y = HEIGHT


all_sprites = pygame.sprite.Group()
player = Student("Make friends")
all_sprites.add(player)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    maze.draw_maze(screen, WHITE)
    player.update()
    pygame.display.flip()

pygame.quit()
