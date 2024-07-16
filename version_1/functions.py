import pyglet as pg
import random
import math
from asteriod import Asteriod

'''
from PIL import Image, ImageFilter

original_image = Image.open('/home/bilal/Desktop/Pyglet_game/resources/Background/bg_3.png')

# Apply a blur filter
blurred_image = original_image.filter(ImageFilter.GaussianBlur(5))

# Save the blurred image to a temporary file
blurred_image.save('blurred_bg.png')
'''

pg.resource.path = ['../resources','../resources/Background','../resources/Asteroids']
pg.resource.reindex()

width = 800
height = 600


# Images 
player_image = pg.resource.image("space_ship.png")
enemy_image  = pg.resource.image("as_2.png")
flame_image  = pg.resource.image("flame.png")
bullet_image = pg.resource.image("bullet.png")

asteriods =[pg.resource.image("as_1.png"),
            pg.resource.image("as_2.png"),
            pg.resource.image("as_3.png"),
            pg.resource.image("as_4.png")]

bgs = [pg.resource.image("bg_1.jpg"),
       pg.resource.image("bg_2.png"),
       pg.resource.image("bg_3.png"),
       pg.resource.image("bg_5.jpg")]

def get_bg(bgs):
    bg = random.choice(bgs)
    # bg = bgs[2]
    bg.anchor_x = random.randint(0,bg.width - width)
    bg.anchor_y =  random.randint(0,bg.height - height)
    return bg

bullet_image.anchor_x =  bullet_image.width / 10
bullet_image.anchor_y =  bullet_image.height / 2

flame_image.anchor_x = flame_image.width  / 2
flame_image.anchor_y = flame_image.height * 1.8

def collisions(game_objects):
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision(obj_2)
                    obj_2.handle_collision(obj_1)
    s_c = 0
    to_remove = [obj for obj in game_objects if obj.dead]
    for obj in to_remove:
        obj.delete()
        game_objects.remove(obj)
        
        if obj.__class__.__name__ == "Asteriod":
            s_c += obj.scale
    
    
        if obj.__class__.__name__ == 'Player':
            if obj.dead == True:
                return -1

    return s_c
            
            
def centre_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

# Generate enemys at random Positions
def enemy(num_enemy, player_position, main_batch=None):
    enemys = []
    for i in range(num_enemy):
        enemy_x, enemy_y = player_position
        
        while distance((enemy_x, enemy_y), player_position) < 100:
            enemy_x = random.randint(0, 800)
            enemy_y = random.randint(0, 600)
        asteriod_image = random.choice(asteriods)
        centre_image(asteriod_image)
        new_enemy = Asteriod(image=asteriod_image, x=enemy_x, y=enemy_y, batch=main_batch)
        new_enemy.rotation   = random.randint(0, 360)
        new_enemy.velocity_x = random.random() * 40
        new_enemy.velocity_y = random.random() * 40

        enemys.append(new_enemy)
    return enemys

# Distance Between player and enemy
def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)

