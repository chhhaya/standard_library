__version__ = 1,3

class Widget:
    def __init__(self, name):
        self.name = name
        self.x = 50
        self.y = 50

    def size(self):
        return self.x, self.y

    def resize(self, x, y):
        self.x = x
        self.y = y
