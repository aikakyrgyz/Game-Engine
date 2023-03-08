import datetime
# >>> b = datetime.datetime.now()
# >>> delta = b - a
# >>> print delta
# 0:00:05.077263
# >>> int(delta.total_seconds() * 1000) # milliseconds
# 5077

class TMGE:
    def __init__(self, FPS, GUI):
        self.game_objects = []
        self.tile_board = None
        self.game_pause= False
        self.setFPS(FPS)
        self.GUI = GUI # would update the drawing and the game window itself, such as score and time.



    def setFPS(self, FPS):
        self.FPS = FPS


    def time_between_updates(self):
        # 1s = 1000 ms
        self.delta = 1000/60


    def add_game_object(self, game_object):
        self.game_objects.append(game_object)


    def run(self):
        last_update = datetime.datetime.now() * 1000
        while not self.game_pause:
            while(datetime.datetime.now()*1000 - last_update > self.delta):
                self.update()

    def update(self):
        self.tile_board.update()
        self.update_dashboard()
        self.gui.update()
            # a dashboard has a game object that belongs to it
            # game_object.update() # each game object should have their own defintion of update
            # maybe we just add mario just standing moving the hand or smth
            # so update would animate it









