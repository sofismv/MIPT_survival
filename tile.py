import pygame
import random
from wall import Wall


# Данный класс представляет собой одну ячейку поля лабиринта
# Каждая ячейка хранит своих соседей
class Tile(pygame.Rect):
    widthTile = 0
    heightTile = 0
    total_tiles = 1

    def __init__(self, width, height, x=0, y=0):
        self.idTile = Tile.total_tiles  # храним номер ячейки
        self.neighbors = list()
        self.walls = list()
        self.fully_visited = False
        self.color = 'black'
        self.x = x
        self.y = y

        Tile.total_tiles += 1

        Tile.widthTile = width
        Tile.heightTile = height

        pygame.Rect.__init__(self, (x, y), (Tile.widthTile, Tile.heightTile))

    def add_neighbor(self, tile):
        if tile not in self.neighbors:
            self.neighbors.append(tile)
            random.shuffle(self.neighbors)  # для создания различных рандомно генерирующихся лабиринтов

    def add_wall(self, horizontal, vertical):
        if horizontal:
            x = self.x
            y = self.y + Tile.heightTile
            height = 7
            width = Tile.widthTile
            self.walls.append(Wall(x, y, width, height, True))

        if vertical:
            x = self.x + Tile.widthTile
            y = self.y
            height = Tile.heightTile
            width = 7
            self.walls.append(Wall(x, y, width, height, False))

    def draw_tile_walls(self, screen, color):
        for i in range(0, len(self.walls)):
            self.walls[i].draw_wall(screen, color)

    def remove_wall_(self, direVertical):
        for i in range(0, len(self.walls)):
            if direVertical and self.walls[i].vertical:
                self.walls[i].remove_wall()
            elif (not direVertical) and self.walls[i].horizontal:
                self.walls[i].remove_wall()

    @staticmethod
    def reset():
        Tile.total_tiles = 1
        Tile.widthTile = 0
        Tile.heightTile = 0

    # Смотрим, можем ли мы пройти через данную ячейку
    def is_walkable(self, x, y, key_state):
        for i in range(0, len(self.walls)):
            if self.walls[i].is_blocked(x, y, key_state):
                return False
        return True