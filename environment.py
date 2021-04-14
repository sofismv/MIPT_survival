import pygame
import sys
from maze import Maze
from student import Student
from question import Question

mainClock = pygame.time.Clock()
from pygame.locals import *

WIDTH = 900
HEIGHT = 700
FPS = 60
mazeSize = 20
WHITE = (0, 0, 0)
BLACK = (229, 204, 255)
RED = (255, 0, 0)
PURPLE = (204, 204, 255)

maze = Maze(mazeSize, WIDTH, HEIGHT)
pygame.init()
pygame.display.set_caption('MIPT survival')
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont(None, 48)
font2 = pygame.font.SysFont(None, 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

all_sprites = pygame.sprite.Group()
player = Student()
all_sprites.add(player)


all_sprites = pygame.sprite.Group()
player = Student()
all_sprites.add(player)

click = False


def main_menu():
    for level in range(1, 9):
        current_level = True
        count_games = 0
        while current_level:
            level_size = 15
            game_number = 0
            screen.fill(BLACK)
            draw_text(str(level) + ' semester', font, WHITE, screen, 370, 20)
            draw_text('mark: ' + str(player.current_mark()), font2, WHITE, screen, 800, 50)
            draw_text('health: ' + str(player.current_health()), font2, WHITE, screen, 800, 80)
            draw_text('pleasure: ' + str(player.current_pleasure()), font2, WHITE, screen, 800, 110)

            mx, my = pygame.mouse.get_pos()

            button_1 = pygame.Rect(50, 100, 400, 50)
            button_2 = pygame.Rect(50, 200, 400, 50)
            button_3 = pygame.Rect(50, 300, 400, 50)

            if button_1.collidepoint((mx, my)):
                if click:
                    game_health()
                    count_games += 1
                    if count_games == 3:
                        current_level = False
            if button_2.collidepoint((mx, my)):
                if click:
                    game_intelligence()
                    count_games += 1
                    if count_games == 3:
                        current_level = False
            if button_3.collidepoint((mx, my)):
                if click:
                    game_socialization()
                    count_games += 1
                    if count_games == 3:
                        current_level = False
            pygame.draw.rect(screen, PURPLE, button_1)
            pygame.draw.rect(screen, PURPLE, button_2)
            pygame.draw.rect(screen, PURPLE, button_3)
            draw_text('get healthier', font, WHITE, screen, 60, 110)
            draw_text('make yourself smarter', font, WHITE, screen, 60, 210)
            draw_text('make more friends', font, WHITE, screen, 60, 310)
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                        game_number += 1
                        pygame.display.flip()
                        pygame.display.update()
                        if game_number > 3:
                            current_level = False

            pygame.display.update()
            mainClock.tick(60)


def game_health():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if player.finish == True:
                player.change_health(5)
                player.finish = False
                player.rect.x = 0
                player.rect.y = 0
                running = False

        screen.fill(BLACK)
        maze.draw_maze(screen, WHITE)
        all_sprites.draw(screen)
        all_sprites.update(maze)
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)


def game_intelligence():
    running = True
    questions = pygame.sprite.Group()
    for i in range (15):
        new_question = Question()
        questions.add(new_question)
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if player.finish == True:
                player.finish = False
                player.rect.x = 0
                player.rect.y = 0
                running = False
            for new_question in questions:
                if pygame.sprite.spritecollideany(new_question, all_sprites):
                    new_question.kill()




        screen.fill(BLACK)
        maze.draw_maze(screen, WHITE)
        all_sprites.draw(screen)
        questions.draw(screen)
        player.update(maze)
        questions.update()
        pygame.display.flip()

        pygame.display.update()
        mainClock.tick(10)


def game_socialization():
    running = True
    questions = pygame.sprite.Group()
    for i in range(15):
        new_question = Question()
        questions.add(new_question)
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if player.finish == True:
                player.finish = False
                player.rect.x = 0
                player.rect.y = 0
                running = False
            for new_question in questions:
                if pygame.sprite.spritecollideany(new_question, all_sprites):
                    new_question.kill()





        screen.fill(BLACK)
        maze.draw_maze(screen, WHITE)
        all_sprites.draw(screen)
        questions.draw(screen)
        all_sprites.update(maze)

        questions.update()
        pygame.display.flip()

        pygame.display.update()
        mainClock.tick(60)



main_menu()
