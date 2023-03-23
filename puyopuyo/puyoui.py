import pygame

from puyopuyo.puyogameplay import PuyoGame
from engine.GUI.gui import GUI


def start_menu_1p(player1):
    puyo_puyo_gui = GUI()
    puyo_puyo_game = PuyoGame(FPS=0.2, GUI=puyo_puyo_gui)
    puyo_puyo_game.run()


def start_menu_2p(player1, player2):
    puyo_puyo_gui = GUI()
    puyo_puyo_game = PuyoGame(FPS=0.2, GUI=puyo_puyo_gui)
    puyo_puyo_game.run()


class PuyoPuyoUI(GUI):
    def __init__(self):
        super().__init__()
