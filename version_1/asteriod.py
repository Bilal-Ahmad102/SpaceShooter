from physicalObject import PhysicalObject
import random

class Asteriod(PhysicalObject):
    def __init__(self,image,*args,**kwargs):
        super().__init__(image,*args,**kwargs)
        self.rotation = random.randint(0,360)
        
    def handle_collision(self, other):
        if not self.dead:
            if self.scale > 0.25:
                num_asteroids = random.randint(2, 3)
                for _ in range(num_asteroids):
                    new_asteroid = Asteriod(image=self.image, x=self.x, y=self.y, batch=self.batch)
                    new_asteroid.velocity_x = (random.random() * 70 - 35) + self.velocity_x
                    new_asteroid.velocity_y = (random.random() * 70 - 35) + self.velocity_y
                    new_asteroid.scale = self.scale * 0.5
                    self.new_objects.append(new_asteroid)
            self.asteriod_dead = True

            
    def update(self,dt):
        super(Asteriod,self).update(dt)
        self.rotation = self.rotation * dt