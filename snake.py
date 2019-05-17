from random import randint

class Snake:
    def __init__(self, game):
        x = randint(0, game.size - 1)
        y = randint(0, game.size - 3)
        self.segment = []
        self.segment.append((x, y))
        self.segment.append((x, y + 1))
        self.segment.append((x, y + 2))

    def moveLeft(self, apple):
        x, y = self.segment[0]
        head = (x, y - 1)
        self.segment = [head] + self.segment
        x, y = head
        Ax, Ay = apple
        if Ax == x and Ay == y:
            return
        del self.segment[-1]

    def moveRight(self, apple):
        x, y = self.segment[0]
        head = (x, y + 1)
        self.segment = [head] + self.segment
        x, y = head
        Ax, Ay = apple
        if Ax == x and Ay == y:
            return
        del self.segment[-1]

    def moveUp(self, apple):
        x, y = self.segment[0]
        head = (x - 1, y)
        self.segment = [head] + self.segment
        x, y = head
        Ax, Ay = apple
        if Ax == x and Ay == y:
            return
        del self.segment[-1]

    def moveDown(self, apple):
        x, y = self.segment[0]
        head = (x + 1, y)
        self.segment = [head] + self.segment
        x, y = head
        Ax, Ay = apple
        if Ax == x and Ay == y:
            return
        del self.segment[-1]








