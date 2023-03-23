from drmario.dmgameplay import DrMarioGame
from engine.GUI.gui import GUI


def start_menu():
    print("Dr. Mario started!")
    dr_mario_gui = GUI()
    dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
    dr_mario_game.run()


class DrMarioUI(GUI):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    start_menu()
