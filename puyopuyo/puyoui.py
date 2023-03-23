import pygame
from database import score
from puyopuyo.puyogameplay import PuyoGame
from engine.GUI.gui import GUI


def start_menu_1p(player1):
    puyo_puyo_gui = GUI()
    puyo_puyo_game = PuyoGame(FPS=0.2, GUI=puyo_puyo_gui)
    score1 = puyo_puyo_game.run()
    score.insert_puyo_score(player1, score1)



def start_menu_2p(player1, player2):
    pygame.init()
    puyo_puyo_gui = GUI()
    puyo_puyo_game = PuyoGame(FPS=0.2, GUI=puyo_puyo_gui)
    score1 = puyo_puyo_game.run()
    score.insert_puyo_score(player1, score1)

    pause_for_second_player()

    score2 = puyo_puyo_game.run()
    score.insert_puyo_score(player2, score2)

    score.compare_puyo_score(player1, player2)


def pause_for_second_player():
    print("1st Player GAME OVER. Press Enter for 2nd Player Game")
    input()


class PuyoPuyoUI(GUI):
    def __init__(self):
        super().__init__()
