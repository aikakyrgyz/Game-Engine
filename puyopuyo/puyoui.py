from database import score
from puyopuyo.puyogameplay import PuyoGame
from engine.GUI.gui import GUI


def start_menu_1p(player1):
    puyo_puyo_gui = GUI()
    puyo_puyo_game = PuyoGame(FPS=0.2, GUI=puyo_puyo_gui)
    score1 = puyo_puyo_game.run()
    score.insert_dm_score(player1, score1)

# Currently when the run function is called, the game just starts a new one as soon as the ending condition is met.
# Need a way to pause in-between so the second player can play and also have their score inserted.
# Then a victory screen at the end? The SQL comparison functions are already written.

# def start_menu_2p(player1, player2):
#     puyo_puyo_gui = GUI()
#     puyo_puyo_game = PuyoGame(FPS=0.2, GUI=puyo_puyo_gui)
#     score1 = puyo_puyo_game.run()
#     score.insert_dm_score(player1, score1)
#     score2 = puyo_puyo_game.run()
#     score.insert_dm_score(player1, score2)


class PuyoPuyoUI(GUI):
    def __init__(self):
        super().__init__()
