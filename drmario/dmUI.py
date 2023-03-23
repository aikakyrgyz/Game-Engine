import pygame

from drmario.dmgameplay import DrMarioGame
from engine.GUI.gui import GUI

game_over_font = pygame.font.SysFont("calibri", 20)
game_over = False


def start_menu():
    print("Dr. Mario started!")
    dr_mario_gui = GUI()
    dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
    dr_mario_game.run()


class DrMarioUI(GUI):
    def __init__(self):
        super().__init__()


def game_over():
    display_game_over = game_over_font.render("Game Over", True)
    pass


if __name__ == '__main__':
    start_menu()
