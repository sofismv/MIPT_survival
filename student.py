import pygame
from tile import Tile
from maze import Maze

WHITE = (255, 255, 255)
BLUE = (51, 153, 255)
WIDTH = 900
HEIGHT = 700
mazeSize = 20


class Student(pygame.sprite.Sprite):
    live_goal = "none"
    socialization_level = 5
    mark = 5
    health = 3
    pleasure = 5
    scholarship = 1000
    finish = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH // mazeSize, HEIGHT // mazeSize))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedx = 0
        self.speedy = 0
        self.finish = False

    def update(self, maze):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -WIDTH // mazeSize
        if keystate[pygame.K_RIGHT]:
            self.speedx = WIDTH // mazeSize
        if keystate[pygame.K_UP]:
            self.speedy = -HEIGHT // mazeSize
        if keystate[pygame.K_DOWN]:
            self.speedy = HEIGHT // mazeSize


        if self.rect.x + self.speedx < 0:
            self.rect.x = 0
        elif self.rect.y + self.speedy < 0:
            self.rect.y = 0
        elif (self.rect.x + self.speedx + 45) > WIDTH:
            self.rect.x = WIDTH - WIDTH // mazeSize
        elif (self.rect.y + self.speedy + 35) > HEIGHT:
            self.rect.y = HEIGHT - HEIGHT // mazeSize
        elif Maze.walkable(maze, self.rect.x, self.rect.y, keystate):
            self.rect.x += self.speedx
            self.rect.y += self.speedy

        if self.rect.x == WIDTH - WIDTH // mazeSize and self.rect.y ==  HEIGHT - HEIGHT // mazeSize:
            self.finish = True

    def change_life_goal(self, new_goal):
        Student.life_goal = new_goal

    def change_mark(self, value):
        Student.mark = max(Student.mark + value, 10)
        if Student.mark <= 2:
            print("It seems someone was expelled. Start over")

    def change_health(self, value):
        Student.health = max(Student.health + value, 3)
        if Student.health < 1:
            print("Unfortunately, your heart couldn't take this life")

    def change_pleasure(self, value):
        Student.pleasure = max(0, Student.pleasure + value)

    def change_socialization_level(self, value):
        Student.socialization_level = max(0, Student.socialization_level + value)

    def change_scholarship(self, value):
        Student.scholarship += value

    def current_mark(self):
        return Student.mark

    def current_health(self):
        return Student.health

    def current_pleasure(self):
        return Student.pleasure

    def current_socialization_level(self):
        return Student.socialization_level

    def current_scholarship(self):
        return Student.scholarship