#!/usr/bin/python3
# (c) starktm1 a.k.a AlenPaulVarghese
import os
import shutil
import time

home = os.getcwd().split('/')[:3]
HOME = (f'/{home[1]}/{home[2]}')

wallpapper_folder = os.path.join(HOME, ".local/share/backgrounds/")
temp_folder = os.path.join(HOME, ".local/share/backgrounds/temp/wall.jpeg")


def copy(source):
    shutil.copy(source, temp_folder)


def mover(source):
    shutil.move(source, wallpapper_folder)


def delete(source):
    os.remove(source)


while True:
    for file in os.listdir(f'{HOME}/Pictures/wallpaper'):
        path_of_file = os.path.join(f'{HOME}/Pictures/wallpaper', file)
        if (os.path.isfile(path_of_file)) and (path_of_file != os.path.join(f'{HOME}/Pictures/wallpaper', 'auto_wallpaper.py')):
            print(path_of_file)
            copy(path_of_file)
            delete(os.path.join(wallpapper_folder, 'wall.jpeg'))
            mover(temp_folder)
            # Change The Value As Your Likings
            time.sleep(100)
