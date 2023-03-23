import os
import sys
# sys.path.append(r'/Users/okdrahcir/documents/github/Inf-122-Final-Project')
# sys.path.append(r'/Users/aigerimkubanychbekova/Desktop/final-women/Inf-122-Final-Project')
# if you are having a engine moduleNotFound error, you will have to include the root directory path to sys.path
from puyopuyo.puyoTileBoard import PuyoTileBoard
from engine.Sprite.sprite import Sprite
from engine.Board.tiles_board import TilesBoard
from engine.GUI.gui import GUI
from engine.TMGE import TMGE
from engine.Tile.tileAbstractFactory import TileAbstractFactory
from engine.Tile.tileFactory import TileFactory
from puyopuyo.myTiles.Blue import Blue
from puyopuyo.myTiles.Green import Green
from puyopuyo.myTiles.Orange import Orange

import pygame

class PuyoGame(TMGE):
    # to do: Singleton Pattern to make sure only one instance of TMGE is created

    def __init__(self, FPS, GUI):
        TMGE.__init__(self, FPS, GUI)

        #puyopuyo starts with an empty board always
        self.tile_types = [["E", "E", "E"],["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"],["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"]] #vertical matching case 2

        self.tile_size = 20
        # the reason why we want them to be produced from the same factories is for matching purposes.
        self.falling_tile_types = ["G", "B", "O"]  # A = green puyo # B = blue puyo

    def overriden(f): # this is just for marking the function as a defined abstract function
        return f

    @overriden
    def set_up_my_game(self):
        self.create_my_tile_board()

    def create_my_tile_board(self):
        self.set_up_my_tile_factories()
        self.set_up_my_falling_tile_factories()
        my_tile_board = PuyoTileBoard(self.tile_size,
                                      self.factory, self.falling_factory,
                                      self.tile_types, self.falling_tile_types,
                                      2, 2, 3, 1, 2)
        self.set_tile_board(my_tile_board)

    #pre-setup of the tile factory
    def set_up_my_tile_factories(self):
        # create the main factory
        factory = TileAbstractFactory()
        # initialize each inidividual factory
        # green_factory = TileFactory(Green, Sprite("images/green-puyo.png"), "G", False)
        # blue_factory = TileFactory(Blue, Sprite("images/blue-puyo.png"), "B", False)
        green_factory = TileFactory(Green, Sprite("green-puyo.png"), "G", False)
        blue_factory = TileFactory(Blue, Sprite("blue-puyo.png"), "B", False)
        orange_factory = TileFactory(Orange, Sprite("orange-tile.png"), "O", False)
        # register individual factories within the main factory
        factory.register_factory("G", green_factory)
        factory.register_factory("B", blue_factory)
        factory.register_factory("O", orange_factory)
        self.set_factory(factory)

    def set_up_my_falling_tile_factories(self):
        falling_factory = TileAbstractFactory()
        
        # green_factory = TileFactory(Green, Sprite("images/green-pill.png"), "A", False)
        # blue_factory = TileFactory(Blue, Sprite("images/blue-pill.png"), "B", False)
        green_factory = TileFactory(Green, Sprite("green-pill.png"), "A", False)
        blue_factory = TileFactory(Blue, Sprite("blue-pill.png"), "B", False)
        orange_factory = TileFactory(Orange, Sprite("orange-tile.png"), "C", False)

        falling_factory.register_factory("G", green_factory)
        falling_factory.register_factory("B", blue_factory)
        falling_factory.register_factory("O", orange_factory)
        
        self.set_falling_factory(falling_factory)

    def set_factory(self, factory):
        self.factory = factory

    def set_falling_factory(self, factory):
        self.falling_factory = factory

    def get_tile_types(self):
        return self.tile_types

    def get_falling_tile_types(self):
        return self.falling_tile_types


if __name__ == '__main__':
    pygame.init()
    myGUI = GUI()
    myPuyoGame = PuyoGame(60, myGUI)
    myPuyoGame.run()


