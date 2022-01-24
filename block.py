from random import randint

class Block:
    def __init__(self):
        self.r = randint(0, 250)
        self.g = randint(0, 250)
        self.b = randint(0, 250)

    def get_rgb(self):
        return [self.r, self.g, self.b]