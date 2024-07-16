import math
import pyglet as pg

class PhysicalObject(pg.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.dead = False
        self.new_objects = []
        self.is_bullet = False 
        self.react_to_bullets = True
        self.asteriod_dead = False
        
    def distance(self, point_1=(0, 0), point_2=(0, 0)):
        """Returns the distance between two points"""
        return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

    def collides_with(self, other):
        if not self.react_to_bullets and other.is_bullet:
            return False
        if self.is_bullet and not other.react_to_bullets:
            return False
        if self.__class__ == other.__class__:
            return False
        
        collision_distance = self.image.width / 2 + other.image.width / 2
        actual_distance = self.distance(self.position, other.position)
        return actual_distance <= collision_distance

    def handle_collision(self, other_object):
        self.dead = True

    def check_bounds(self):
        min_x = 0   + 10
        min_y = 0   + 10
        max_x = 800 - 10
        max_y = 600 - 10

        if self.x < min_x:
            self.velocity_x = - self.velocity_x 
        elif self.x > max_x:
            self.velocity_x = - self.velocity_x

        if self.y < min_y:
            self.velocity_y = - self.velocity_y
        elif self.y > max_y:
            self.velocity_y = - self.velocity_y

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_bounds()
