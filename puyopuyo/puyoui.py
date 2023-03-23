from puyopuyo.puyogameplay import PuyoGame
from engine.GUI.gui import GUI


def start_menu():
    print("Puyo Puyo started!")
    puyo_puyo_gui = GUI()
    puyo_puyo_game = PuyoGame(FPS=0.2, GUI=puyo_puyo_gui)
    puyo_puyo_game.run()


class PuyoPuyoUI(GUI):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    start_menu()
