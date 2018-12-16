

class Sprite(object):
    def __init__(self, startX, startY):
        self.x = startX
        self.y = startY
    def move(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY
    def draw(self):
        pass

