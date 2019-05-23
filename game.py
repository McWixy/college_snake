from random import randint
from snake import Snake

class Game:
    def __init__(self, game_size : int):
        self.size = game_size
        self.map = []
        for _ in range(self.size):
            ligne = []
            for _ in range(self.size):
                ligne.append(0)
            self.map.append(ligne)
        self.pomme_is_there = False

    def __repr__(self):
        info = "[ Game of size " 
        info += str(self.size) 
        info += " ]"
        return info

    def set_snake(self, snake):
        self.snake = snake
        for x, y in self.snake.segment:
            self.map[x][y] = 2

    def show_game(self):
        for i in range(self.size):
            for j in range(self.size):
                Ax, Ay = self.apple
                if self.snake_there(i, j):
                    print('S', end=' ')
                elif Ax == i and Ay == j:
                    print('#', end=' ')
                else:
                    print('.', end=' ')
            print()

    def snake_there(self, x, y):
        liste = self.snake.segment
        for segment in liste:
            Sx, Sy = segment
            if Sx == x and Sy == y:
                return True
        return False

    def add_apple(self):
        if self.pomme_is_there == False:
            while True:
                x = randint(0, self.size - 1)
                y = randint(0, self.size - 1)
                if self.snake_there(x, y) == True:
                    continue
                self.apple = (x, y)
                print(self.apple)
                break
            self.pomme_is_there = True
            
    def set_snake(self, snake):
        self.snake = snake
        print(self.snake.segment)
        for x, y in self.snake.segment:
            self.map[x][y] = 2

    def update_game(self):
        direction = input("Direction")
        print('a')
        """
            a/q => gauche = 1
            d/d => droite = 2
            w/z => haut   = 3
            s/s => bas    = 4
        """
        if direction == "a":
            self.snake.moveLeft(self.apple)
        elif direction == "d":
            self.snake.moveRight(self.apple)
        elif direction == "w":
            self.snake.moveUp(self.apple)
        elif direction == "s":
            self.snake.moveDown(self.apple)


















