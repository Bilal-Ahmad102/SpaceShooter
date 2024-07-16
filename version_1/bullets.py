from physicalObject import PhysicalObject

class Bullets(PhysicalObject):
    def __init__(self, image, *args, **kwargs):
        super(Bullets, self).__init__(img=image, *args, **kwargs)
        self.is_bullet = True
    def check_bounds(self):
        # New implementation for check_bounds
        min_x = -10
        min_y = -10
        max_x = 810
        max_y = 610

        if self.x < min_x or self.x > max_x or self.y < min_y or self.y > max_y:
            self.dead = True

    def update(self, dt):
        super(Bullets, self).update(dt)
        self.check_bounds()
