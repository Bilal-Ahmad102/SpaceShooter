import math
import pyglet as pg 
from pyglet.window import key
from physicalObject import PhysicalObject
from functions import flame_image, bullet_image
from bullets import Bullets

class Player(PhysicalObject):
    def __init__(self, player_image, *args, **kwargs):
        super().__init__(img=player_image, *args, **kwargs)
        self.x = 400
        self.y = 300
        self.thrust = 300.0
        self.rotation_speed = 300.0
        self.bullet_speed = 700.0
        self.key_handler = key.KeyStateHandler()
        self.flame_sprite = pg.sprite.Sprite(img=flame_image, *args, **kwargs)
        self.flame_sprite.visible = False
        self.react_to_bullets = False
        self.lives_left = 5
        self.life_sprites = []
        self.create_life_sprites()

    def create_life_sprites(self):
        for i in range(self.lives_left):
            life_sprite = pg.sprite.Sprite(img=self.image, x=785-i*30, y=585, batch=self.batch)
            life_sprite.rotation = -90
            life_sprite.scale = 0.5
            self.life_sprites.append(life_sprite)

    def update_life_display(self):
        for i, sprite in enumerate(self.life_sprites):
            if i < self.lives_left:
                sprite.visible = True
            else:
                sprite.visible = False

    def handle_collision(self, other_object):
        if self.lives_left > 0:
            self.lives_left -= 1
            self.update_life_display()
            # Reset player position
            self.x = 400
            self.y = 300
            self.velocity_x = 0
            self.velocity_y = 0
            self.rotation = 0
        else:
            self.dead = True

    def delete(self):
        for sprite in self.life_sprites:
            sprite.delete()
        self.flame_sprite.delete()
        super(Player, self).delete()

    def fire(self):
        """first convert the degree of rotation to radian and  negate it, 
        because Pyglet calculate degree opposite.
        then with radius and angle of rotation of player, we can calculate corresponding coordinate on the 
        circle around the player, using that coordinate we will calculate the starting point of bullets.
        """
        angle_radian = -math.radians(self.rotation)
        ship_radius = self.image.width/2
        bullet_x = self.x  + math.cos(angle_radian) * ship_radius 
        bullet_y = self.y  + math.sin(angle_radian) * ship_radius 

        new_bullet = Bullets(bullet_image, x=bullet_x, y=bullet_y, batch=self.batch)

        bullet_vx = (self.velocity_x + math.cos(angle_radian) * self.bullet_speed)
        bullet_vy = (self.velocity_y + math.sin(angle_radian) * self.bullet_speed)

        new_bullet.rotation = self.rotation
        
        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy

        self.new_objects.append(new_bullet)
        
        
    
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    def update(self, dt):
        super(Player, self).update(dt)
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotation_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotation_speed * dt

        # if self.key_handler[key.SPACE]:
        #     self.fire()

        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y

            self.flame_sprite.rotation = self.rotation + 90 
            self.flame_sprite.x = self.x
            self.flame_sprite.y = self.y 
            self.flame_sprite.visible = True        
        else:
            self.flame_sprite.visible = False