import pyglet as pg
from pyglet.window import key
from player import Player
from functions import *
from reset import Reset



window = pg.window.Window(width, height)

centre_image(player_image)

score = 0
enemy_num = 20

main_batch = pg.graphics.Batch()
score_label = pg.text.Label(text=f"Score : {score}", x=10, y=window.height-20, batch=main_batch)
level_label = pg.text.Label(text="My Game", x=window.width // 2, y=window.height - 20, anchor_x='center', batch=main_batch)
player_ship = Player(player_image, x=300, y=300, batch=main_batch)
enemys = enemy( enemy_num, player_ship.position, main_batch)

game_objects = enemys + [player_ship]
bg = get_bg(bgs)

def reset_game():
    global main_batch, player_ship, enemys, game_objects, score,bg
    reset_class = Reset(enemy_num)
    main_batch = reset_class.main_batch
    player_ship = reset_class.player_ship
    enemys = reset_class.enemys
    score_label.batch = main_batch
    level_label.batch = main_batch
    bg = get_bg(bgs)
    score_label.text = f"Score : {score}"  # Reset score label text

    game_objects = enemys + [player_ship]
    score = 0

    window.push_handlers(player_ship.key_handler)
    window.push_handlers(player_ship.on_key_press)

def on_key_press(symbol, modifiers):
    if symbol == key.R:
        reset_game()

def update(dt):
    global game_objects, score

    to_add = []
    for obj in game_objects:
        
        obj.update(dt)
        to_add.extend(obj.new_objects)
        if obj.asteriod_dead:
            obj.dead = True
        obj.new_objects = []

    game_objects.extend(to_add)

    add_score = collisions(game_objects)

    if add_score == -1:
        reset_game()
    else:
        score += add_score

    score_label.text = f"Score : {score}"  # Update score label text

    game_objects = [obj for obj in game_objects if not obj.dead]

window.push_handlers(player_ship.key_handler)
window.push_handlers(player_ship.on_key_press)
window.push_handlers(on_key_press)

@window.event
def on_draw():
    window.clear()
    bg.blit(0,0)
    main_batch.draw()

if __name__ == '__main__':
    pg.clock.schedule_interval(update, 1 / 120.0)
    pg.app.run()
