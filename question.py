import pygame
from tile import Tile
from maze import Maze
from random import randint

WIDTH = 900
HEIGHT = 700
mazeSize = 20
COLOUR = (255, 102, 153)

class Question(pygame.sprite.Sprite):
    type = "none"
    height_question = 0
    width_question = 0
    list_question = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH // mazeSize, HEIGHT // mazeSize))
        self.image.fill(COLOUR)
        self.rect = self.image.get_rect()
        place = randint(0, mazeSize*mazeSize - 1)
        self.rect.y = (place//(mazeSize))*(HEIGHT//mazeSize)
        self.rect.x = (place%(mazeSize))*(WIDTH//mazeSize)




        Question.height_question = Tile.heightTile
        Question.width_question = Tile.widthTile

        Question.list_question.append(self)

    def get_question(self, type_):
        randTile = randint(1, len(Maze.tilesMaze))
        question = Question(type_, randTile)
