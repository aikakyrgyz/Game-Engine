from time import time_ns
import time
from math import pow
from abc import ABC, abstractmethod
import pygame

# from Board.tiles_board import TilesBoard
# >>> b = datetime.datetime.now()
# >>> delta = b - a
# >>> print delta
# 0:00:05.077263
# >>> int(delta.total_seconds() * 1000) # milliseconds
# 5077
from engine.Board.tiles_board import TilesBoard


# since TMGE contains one or more abstract functions, it is also an abstract class

class TMGE(ABC):
    def __init__(self, FPS, GUI): # tile_board should not be passed in here
        self.game_objects = []
        self.game_over = False
        self.setFPS(FPS)
        self.GUI = GUI # would update the drawing and the game window itself, such as score and time.

    @abstractmethod
    def set_up_my_game(self):
        pass

    def setFPS(self, FPS):
        self.FPS = FPS

    def time_between_updates(self):
        # 1s = 1000 ms
        self.delta = 1/self.FPS

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    # def run(self):
    #     self.time_between_updates()
    #     last_update = time_ns()
    #     self.set_up_my_game()
    #     self.GUI.draw_board(self.tile_board)
    #     pygame.init() # solely for handling key inputs
    #     while not self.game_over:
    #         self.handle_key_events()
    #         while(time_ns() - last_update > self.delta):
    #             self.update()
    #             last_update += self.delta;
    #             break
    #         self.redraw()


    # run method for testing, otherwise the loop keeps running and I cannot see
    def run(self):
        self.time_between_updates()
        last_update = time_ns()
        self.set_up_my_game()
        
        self.GUI.draw_board(self.tile_board)
        
        pygame.init() # solely for handling key inputs
        
        # GUI testing for Richard, comment the loop to go back out of Richard's testing environment and uncomment the same code below
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.GUI.draw_board(self.tile_board)
            # the initial set of tiles given might already have matches, so need to get rid of them before
            # placing a new falling object
            self.tile_board.match_all()
            # printing just to see if it was matched
            self.GUI.draw_board(self.tile_board)
            # clear the matches
            self.tile_board.clear_out_matches()
            # fill in the holes, if any
            self.tile_board.fill_holes()
            self.GUI.draw_board(self.tile_board)
            
            time.sleep(self.delta)
        
            for i in range(5):
                # updating the tile board for now... for for testing, eventually call the update() function defined for all updates
                self.tile_board.update()
                self.GUI.draw_board(self.tile_board)

        # self.GUI.draw_board(self.tile_board)
        # # the initial set of tiles given might already have matches, so need to get rid of them before
        # # placing a new falling object
        # self.tile_board.match_all()
        # # printing just to see if it was matched
        # self.GUI.draw_board(self.tile_board)
        # # clear the matches
        # self.tile_board.clear_out_matches()
        # # fill in the holes, if any
        # self.tile_board.fill_holes()
        # self.GUI.draw_board(self.tile_board)
        
        # for i in range(5):
        #     # updating the tile board for now... for for testing, eventually call the update() function defined for all updates
        #     self.tile_board.update()
        #     self.GUI.draw_board(self.tile_board)

    def redraw(self):
        self.GUI.draw_board(self.tile_board)
        # draw other parts of the screen

    def set_tile_board(self, board):
        self.tile_board = board

    def update(self):
        self.tile_board.update()
        self.tile_board.add_falling_shape()
        # self.update_dashboard()
        # self.gui.update()
            # a dashboard has a game object that belongs to it
            # game_object.update() # each game object should have their own definition of update
            # falling shape would not really have its own update() function, since the tile board controls it. 
            # maybe we just add mario just standing moving the hand... 
            # so update would animate it

    def handle_key_events(self) -> None:
        """
        Handles each pygame event
        Pressing space, right arrow and left arrow triggers a sound
        """
        for event in pygame.event.get():
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #     self._state.rotate_faller()
            #     self._play_sound('move')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.tile_board.move_left()
                # self._play_sound('move')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.tile_board.move_right()
                # self._play_sound('move')

