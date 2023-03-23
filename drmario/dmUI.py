import pygame

from drmario.dmgameplay import DrMarioGame
from engine.GUI.gui import GUI


def start_menu_1p(player1):
    dr_mario_gui = GUI()
    dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
    dr_mario_game.run()
    # score = dr_mario_game.run()


# def start_menu_2p(player1, player2):
#     dr_mario_gui = GUI()
#     dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
#     score = dr_mario_game.run()
#     insert_dm_score(player1)
#     score = dr_mario_game.run()
#     insert_dm_score(player2)


class DrMarioUI(GUI):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    start_menu_1p()
