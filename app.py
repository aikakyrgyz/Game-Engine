# This is a sample Python script.
import os

import pygame_menu

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from interface import mainmenu as mm
from interface.mainmenu import PROJ_DIR_IMG


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# background image for main menu

def draw_background():
    background_image = pygame_menu.BaseImage(
        # image_path="images_/bg_image.jpg"
        image_path=os.path.join(PROJ_DIR_IMG, 'bg_image.jpg')
    )
    background_image.draw(TMapp.surface)

    # move or adjust this function


def get_game_list_menu():
    # if a database connection exists, use the below
    # return gamesql.return_game_list()
    # if no database connection, use the below
    return [("Dr. Mario", 0, 'mario_image.jpg'), ("Puyo Puyo", 1, 'puyo_image.png')]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    TMapp = mm.MainMenu(title="TM App")
    TMapp.start_menu()
    TMapp.app_menu.mainloop(TMapp.surface, bgfun=draw_background)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
