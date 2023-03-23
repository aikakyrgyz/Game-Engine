import pygame

from drmario.dmgameplay import DrMarioGame
from engine.GUI.gui import GUI


def start_menu_1p(player1):
    dr_mario_gui = GUI()
    dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
    dr_mario_game.run()


def start_menu_2p(player1, player2):
    dr_mario_gui = GUI()
    dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
    dr_mario_game.run()


class DrMarioUI(GUI):
    def __init__(self):
        super().__init__()

