from map import Map
import time
import os
import json
from helicopter import Helicopter as Heli
from pynput import keyboard
from clouds import Clouds


TICK_SLEEP =0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
heli = Heli(MAP_W, MAP_H)
tick = 1


MOVES = {'w': (-1,0), 'd': (0, 1), 's': (1,0), 'a': (0,-1)}
# f - сохранение, g - загрузка
def process_key(key):
    global heli
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        heli.move(dx,dy)
    if c == 'f':
        data = {'helicopter': heli.export_data(), 
                    'clouds': clouds.export_data(), 
                     'field': field.export_data()}
        with open('level.json','w') as lvl:
            json.dump(data, lvl)
        
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

while True:
    os.system('cls')
    field.process_helicopter(heli, clouds)
    heli.print_stats()
    field.print_map(heli, clouds)
    print('TICK',tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()
    