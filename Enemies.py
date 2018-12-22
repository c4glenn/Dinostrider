from sprite import Sprite


class enemy(Sprite):
    def __init__(x, y, width, height, path):
        super().__init__(x, y, height, width)