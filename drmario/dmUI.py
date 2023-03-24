import pygame
from database import score
from drmario.dmgameplay import DrMarioGame
from engine.GUI.gui import GUI


def start_menu_1p(player1):
    dr_mario_gui = GUI()
    dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
    score1 = dr_mario_game.run()
    score.insert_dm_score(player1, score1)


def start_menu_2p(player1, player2):
    pygame.init()
    dr_mario_gui = GUI()
    dr_mario_game = DrMarioGame(FPS=120, GUI=dr_mario_gui)
    score1 = dr_mario_game.run()
    score.insert_dm_score(player1, score1)

    pause_for_second_player()

    score2 = dr_mario_game.run()
    score.insert_dm_score(player2, score2)

    score.compare_dm_score(player1, player2)


def pause_for_second_player():
    print("1st Player GAME OVER. Press Enter for 2nd Player Game")
    input()


class DrMarioUI(GUI):
    def init(self):
        super().init()
