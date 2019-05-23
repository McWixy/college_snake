from random import randint

class Snake:
    def __init__(self, game):
        self.game_size = game.size
        x = randint(0, game.size - 1)
        y = randint(0, game.size - 3)
        self.segment = []
        self.segment.append((x, y))
        self.segment.append((x, y + 1))
        self.segment.append((x, y + 2))

    def ingame(self, segment):
        x, y = segment
        max_size = self.game_size
        if x < 0 or y < 0 or x >= max_size or y >= max_size:
            return False
        return True

    def moveLeft(self, apple):
        x, y = self.segment[0]
        head = (x, y - 1)
        if not self.ingame(head):
            return
        self.segment = [head] + self.segment
        x, y = head
        Ax, Ay = apple
        if Ax == x and Ay == y:
            return
        del self.segment[-1]

    def moveRight(self, apple):
        x, y = self.segment[0]
        head = (x, y + 1)
        if not self.ingame(head):
            return
        self.segment = [head] + self.segment
        x, y = head
        Ax, Ay = apple
        if Ax == x and Ay == y:
            return
        del self.segment[-1]

    def moveUp(self, apple):
        x, y = self.segment[0]
        head = (x - 1, y)
        if not self.ingame(head):
            return
        self.segment = [head] + self.segment
        x, y = head
        Ax, Ay = apple
        if Ax == x and Ay == y:
            return
        del self.segment[-1]

    def moveDown(self, apple):
        x, y = self.segment[0]
        head = (x + 1, y)
        if not self.ingame(head):
            return
        self.segment = [head] + self.segment
        x, y = head
        Ax, Ay = apple
        if Ax == x and Ay == y:
            return
        del self.segment[-1]








