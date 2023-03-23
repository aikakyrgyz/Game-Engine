from time import time_ns
import time
from math import pow
from abc import ABC, abstractmethod
import pygame
import engine.GameObject.direction as Direction

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
    MAX_UPDATES = 1
    def __init__(self, FPS, GUI): # tile_board should not be passed in here
        self.game_objects = []
        self.game_over = False
        self.setFPS(FPS)
        self.GUI = GUI # would update the drawing and the game window itself, such as score and time.
        self.time_between_updates()
        self.last_update = time_ns()
        self.paused = False

    @abstractmethod
    def set_up_my_game(self):
        pass

    def setFPS(self, FPS):
        self.FPS = FPS

    def time_between_updates(self):
        # 1s = 1000 ms
        self.delta = 1000000000/self.FPS

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def run(self):
        self.set_up_my_game()
        # pygame.init() # just initialize in the GUI class
        while not self.paused:
            update_count = 0
            while(time_ns() - self.last_update > self.delta and update_count < self.MAX_UPDATES):
                self.update()
                self.last_update += self.delta
                update_count += 1
                self.redraw()
            time.sleep(1)
            self.handle_key_events()


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
    # def run(self):
    #     self.time_between_updates()
    #     last_update = time_ns()
    #     self.set_up_my_game()
    #     self.GUI.draw_board(self.tile_board)
    #     pygame.init() # solely for handling key inputs
        
        # GUI testing for Richard, comment the loop to go back out of 
        # Richard's testing environment and uncomment the same code below
        # while True:
        #     # checks the board if the condition(tiles passing a specific line) 
        #     # to end game is true
        #     if (self.tile_board.ending_condition()):
        #         return
            
        #     # checks for any key inputs from the player and updates board accordingly
        #     self.handle_key_events()

        #     self.GUI.draw_board(self.tile_board)
        #     # the initial set of tiles given might already have matches, 
        #     # so need to get rid of them before placing a new falling object
        #     self.tile_board.match_all()

        #     # printing just to see if it was matched
        #     self.GUI.draw_board(self.tile_board)

        #     # clear the matches
        #     self.tile_board.clear_out_matches()

        #     # fill in the holes, if any
        #     self.tile_board.fill_holes()
        #     self.GUI.draw_board(self.tile_board)
            
        #     time.sleep(self.delta)
        #     print(self.delta)
        
        #     for i in range(10):
        #         # updating the tile board for now... for for testing, eventually call the update() function defined for all updates
        #         self.tile_board.update()
        #         self.GUI.draw_board(self.tile_board)
        #         time.sleep(self.delta)
        #         print(self.delta)

        # if (self.tile_board.ending_condition()):
        #     return
        #
        # # checks for any key inputs from the player and updates board accordingly
        # # self.handle_key_events()
        #
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
        #
        # for i in range(20):
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
        # self.tile_board.add_falling_shape()
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
            # this line is giving an error: pygame.display not initialized
            # if event.type == pygame.QUIT or pygame.K_ESCAPE:
            #         pygame.quit()
            #         return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.tile_board.move_falling_shape(Direction.LEFT)
                print("left was pressed")
                # self._play_sound('move')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print("right was pressed")
                self.tile_board.move_falling_shape(Direction.RIGHT)
                # self._play_sound('move')
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                print("down was pressed")
                self.tile_board.move_falling_shape(Direction.DOWN)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print("space was pressed")
                self.tile_board.rotate_shape_on_board()
