from Enemies import Enemy


class Slime(Enemy):
    def __init__(self, x, y, Vel, Path):
        super().__init__(x, y, 60, 27, Path, 'Images/Slime', Vel)

    def _get_image(self):
        if self.facing_left:
            return self.images_left[0]
        else:
            return self.images_right[0]
