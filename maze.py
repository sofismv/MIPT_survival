from tile import Tile
import random
import pygame


class Maze(pygame.Rect):
    tilesMaze = {}  # Словарь для хранения всех ячеек лабиринта
    timeExecuted = 1  # Запоминаем время входа во все ячейки
    widthMaze = 0
    heightMaze = 0
    yPos = 0
    xPos = 0
    size_maze = 0

    def __init__(self, sizeMaze__, width, height):
        Maze.widthMaze = width
        Maze.heightMaze = height
        Maze.size_maze = sizeMaze__
        Maze.cost_walk = 10
        tileWidth = width // sizeMaze__
        tileHeight = height // sizeMaze__

        mode = sizeMaze__
        yPos = 0
        xPos = 0
        # Для каждой ячейки определяем x и y координаты
        for idMaze in range(1, (sizeMaze__ * sizeMaze__) + 1):
            if idMaze // mode < 1:
                x = xPos * tileWidth
                y = yPos
                xPos += 1
            else:
                if idMaze // mode == 1:
                    x = xPos * tileWidth
                    y = yPos

                xPos = 0
                yPos += tileHeight
                mode += sizeMaze__

            Maze.tilesMaze[idMaze] = Tile(tileWidth, tileHeight, x, y)

        pygame.Rect.__init__(self, Maze.xPos, Maze.yPos, Maze.widthMaze, Maze.heightMaze)

        self._setNeighbors(sizeMaze__)
        self._setWalls(sizeMaze__)
        self.start = 1
        self.finish = len(self.tilesMaze) - 1

#        randomNode = random.randrange(sizeMaze__ * sizeMaze__) + 1
        randomNode = 1
        self._generateMazeDFS(Maze.tilesMaze[randomNode])
        self._createMultiplePathsRandom()

    # Для каждой ячейки мы определяем её соседей
    def _setNeighbors(self, sizeMaze_):
        for u in range(1, (sizeMaze_ * sizeMaze_) + 1):
            for t in range(1, 3):
                if t == 1:
                    v = u + 1
                else:
                    v = u + sizeMaze_

                if (t == 1 and u % sizeMaze_ != 0) or (t == 2):
                    if u in self.tilesMaze and v in self.tilesMaze:
                        for key, value in self.tilesMaze.items():
                            if key == u:
                                value.add_neighbor(v)
                            if key == v:
                                value.add_neighbor(u)

    # Добавляем все стены (с учетом крайних ячеек), потом будем их удалять
    def _setWalls(self, sizeMaze_):
        mode = sizeMaze_
        for idMaze in range(1, (sizeMaze_ * (sizeMaze_ - 1)) + 1):
            if idMaze // mode < 1:
                self.tilesMaze[idMaze].add_wall(True, True)
            else:
                self.tilesMaze[idMaze].add_wall(True, False)
                mode += sizeMaze_

        for idMaze in range((sizeMaze_ * (sizeMaze_ - 1)) + 1, sizeMaze_ * sizeMaze_):
            self.tilesMaze[idMaze].add_wall(False, True)

    def _print_maze(self, screen, color):
        for key in self.tilesMaze:
            if key < len(self.tilesMaze):
                self.tilesMaze[key].draw_tile_walls(screen, color)

    def draw_maze(self, screen, color):
        pygame.draw.line(screen, color, [0, Maze.heightMaze], [0, 0], 7)
        pygame.draw.line(screen, color, [0, 0], [Maze.widthMaze, 0], 7)
        pygame.draw.line(screen, color, [0, Maze.heightMaze], [Maze.widthMaze, Maze.heightMaze], 7)
        pygame.draw.line(screen, color, [Maze.widthMaze, 0], [Maze.widthMaze, Maze.heightMaze], 7)

        self._print_maze(screen, color)

    # Запускаем DFS из рандомной ячейки, по пути удаляем стены, которые препятствуют прохождению
    def _generateMazeDFS(self, vertex):
        vertex.color = 'red'
        vertex.discoveryTIme = Maze.timeExecuted
        Maze.timeExecuted += 1

        # запускаем для каждого соседа вершины
        for neighbor in vertex.neighbors:
            if Maze.tilesMaze[neighbor].color == 'black':
                vertextToRemoveWall = vertex
                direVertical = True
                if neighbor > vertex.idTile:

                    vertextToRemoveWall = vertex
                    # означает, что мы идём вправо
                    if neighbor - 1 == vertex.idTile:
                        direVertical = True
                    # означает, что мы идём вниз
                    else:
                        direVertical = False
                else:
                    # означает, что мы идём влево
                    if neighbor + 1 == vertex.idTile:
                        vertextToRemoveWall = Maze.tilesMaze[vertex.idTile - 1]
                        direVertical = True
                    # означает, что мы идём вверх
                    else:
                        vertextToRemoveWall = Maze.tilesMaze[vertex.idTile - Maze.size_maze]
                        direVertical = False
                self._removeWall(vertextToRemoveWall, direVertical)
                self._generateMazeDFS(Maze.tilesMaze[neighbor])

        vertex.color = 'blue'
        Maze.timeExecuted += 1

    # Для легкой проходимости делаем так, что удаляем какие-то стены у ячеек с более чем 2 стенами
    def _createMultiplePathsRandom(self):
        for key, value in Maze.tilesMaze.items():
            if len(value.walls) > 2:
                self._removeWall(value, random.choice([True, False]))


    def walkable(self, x, y, keystate):
        x_0 = x//(self.widthMaze // self.size_maze) + 1
        y_0 = y//(self.heightMaze // self.size_maze)
        pos = y_0*self.size_maze + x_0
        if Tile.is_walkable(self.tilesMaze[pos], x, y, keystate) == False:
            return False
        if keystate[pygame.K_RIGHT]:
            return Tile.is_walkable(self.tilesMaze[pos + 1], x, y, keystate)
        elif keystate[pygame.K_LEFT]:
            return Tile.is_walkable(self.tilesMaze[pos - 1], x, y, keystate)
        elif keystate[pygame.K_UP]:
            return Tile.is_walkable(self.tilesMaze[pos - self.size_maze], x, y, keystate)
        elif keystate[pygame.K_DOWN]:
            return Tile.is_walkable(self.tilesMaze[pos + self.size_maze], x, y, keystate)
        return True


    def _removeWall(self, vertex, direVertical):
        vertex.remove_wall_(direVertical)

    def resetMaze(self):
        Maze.timeExecuted = 1
        widthMaze = 0
        Maze.heightMaze = 0
        Maze.yPos = 0
        Maze.xPos = 0
        Maze.size_maze = 0
        Maze.tilesMaze.clear()
        Tile.reset()

    @staticmethod
    def resetTiles():
        for tile in Maze.tilesMaze:
            Maze.tilesMaze[tile].color = 'black'

    @staticmethod
    def get_size_maze():
        return Maze.size_maze