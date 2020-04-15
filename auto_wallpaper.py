#!/usr/bin/python3
import os
import shutil
import time

wallpapper_folder = os.path.join(os.getcwd(),"../../.local/share/backgrounds/")
temp_folder = os.path.join(os.getcwd(),"../../.local/share/backgrounds/temp/wall.jpeg")

def copy(source):
    shutil.copy(source,temp_folder)
def mover(source):
    shutil.move(source,wallpapper_folder)
def delete(source):
    os.remove(source)

while True:
    for file in os.listdir(os.getcwd()):
        path_of_file = os.path.join(os.getcwd(),file)
        if (os.path.isfile(path_of_file)) and (path_of_file!=os.path.join(os.getcwd(),'auto_wallpaper.py')):
            print(path_of_file)
            copy(path_of_file)
            delete(os.path.join(wallpapper_folder,'wall.jpeg'))
            mover(temp_folder)
            # Change The Value As Your Likings
            time.sleep(200)
        
