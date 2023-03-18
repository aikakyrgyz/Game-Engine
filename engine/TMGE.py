from time import time_ns
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
        self.delta = pow(10, 9)/self.FPS

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

    # run method for testing, otherwise the loop keeps running and I cannot see lol
    def run(self):
        self.time_between_updates()
        last_update = time_ns()
        self.set_up_my_game()
        self.GUI.draw_board(self.tile_board)

        pygame.init() # solely for handling key inputs


        self.GUI.draw_board(self.tile_board)
        self.tile_board.add_falling_shape()

        for i in range(5):
            self.tile_board.update()
            self.GUI.draw_board(self.tile_board)


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
            # game_object.update() # each game object should have their own defintion of update
            # maybe we just add mario just standing moving the hand or smth
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

