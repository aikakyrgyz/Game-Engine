from database import score
from drmario.dmgameplay import DrMarioGame
from engine.GUI.gui import GUI


def start_menu_1p(player1):
    dr_mario_gui = GUI()
    dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
    score1 = dr_mario_game.run()
    score.insert_dm_score(player1, score1)

# Currently when the run function is called, the game just starts a new one as soon as the ending condition is met.
# Need a way to pause in-between so the second player can play and also have their score inserted.
# Then a victory screen at the end? The SQL comparison functions are already written.

# def start_menu_2p(player1, player2):
#     dr_mario_gui = GUI()
#     dr_mario_game = DrMarioGame(FPS=0.2, GUI=dr_mario_gui)
#     score1 = dr_mario_game.run()
#     score.insert_dm_score(player1, score1)
#     score2 = dr_mario_game.run()
#     score.insert_dm_score(player2, score2)


class DrMarioUI(GUI):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    start_menu_1p()
