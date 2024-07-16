# reset.py
import pyglet as pg
from player import Player
from functions import enemy, player_image

class Reset:
    def __init__(self, enemy_num):
        self.main_batch = pg.graphics.Batch()
        self.player_ship = Player(player_image, x=300, y=300, batch=self.main_batch)
        self.enemys = enemy( enemy_num, self.player_ship.position, self.main_batch)

    def get_game_objects(self):
        return self.enemys + [self.player_ship]
