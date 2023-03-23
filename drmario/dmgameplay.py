import os
import sys

# sys.path.append(r'/Users/okdrahcir/documents/github/Inf-122-Final-Project')

# if you are having a engine moduleNotFound error, you will have to include the root directory path to sys.path
# sys.path.append(r'/Users/aigerimkubanychbekova/Desktop/final-women/Inf-122-Final-Project')
# if you are having an engine moduleNotFound error, you will have to include the root directory path to sys.path

from drmario.dmTileBoard import DMTileBoard
from engine.Sprite.sprite import Sprite
from engine.GUI.gui import GUI
from engine.TMGE import TMGE
from engine.Tile.tileAbstractFactory import TileAbstractFactory
from engine.Tile.tileFactory import TileFactory
from drmario.myTiles.Yellow import Yellow
from drmario.myTiles.Red import Red


class DrMarioGame(TMGE):
    # to do: Singleton Pattern to make sure only one instance of TMGE is created

    def __init__(self, FPS, GUI):
        TMGE.__init__(self, FPS, GUI)

        # testing
        # self.tile_types = [["E", "E", "E"],["E", "E", "E"],["E", "E", "E"], ["E", "R", "E"], ["Y", "Y", "Y"]]
        # self.tile_types = [["E", "E", "E"],["E", "E", "Y"],["E", "E", "Y"], ["E", "Y", "R"], ["Y", "Y", "Y"]]

        # vertical matching
        # self.tile_types = [["E", "E", "E"],["E", "E", "Y"], ["E", "E", "Y"], ["E", "E", "Y"], ["E", "E", "R"],["E", "E", "Y"], ["E", "R", "Y"], ["Y", "R", "Y"]] #vertical matching
        # self.tile_types = [["E", "E", "E"],["E", "E", "Y"], ["E", "E", "Y"], ["E", "E", "Y"], ["E", "E", "Y"],["E", "E", "Y"], ["E", "R", "Y"], ["Y", "R", "R"]] #vertical matching case 1
        # self.tile_types = [["E", "E", "E"],["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"], ["E", "R", "E"],["E", "R", "E"], ["E", "R", "E"], ["Y", "Y", "E"]] #vertical matching case 1
        # self.tile_types = [["E", "E", "E"],["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"], ["E", "R", "E"],["E", "R", "E"], ["E", "R", "E"], ["Y", "R", "E"]] #vertical matching case 2
        # self.tile_types = [["E", "E", "E"],["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"], ["E", "R", "E"],["E", "Y", "E"], ["E", "R", "E"], ["Y", "R", "E"]] #vertical matching case 3
        # self.tile_types = [["E", "E", "E"],["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"], ["E", "R", "Y"],["E", "Y", "Y"], ["E", "R", "Y"], ["Y", "R", "Y"]] #vertical matching case 4
        # self.tile_types = [["E", "E", "E"],["E", "E", "Y"], ["E", "E", "Y"], ["E", "E", "Y"], ["E", "R", "R"],["E", "Y", "Y"], ["E", "R", "Y"], ["Y", "R", "Y"]] #vertical matching case 5
        # self.tile_types = [["E", "E", "E"],["E", "E", "Y"], ["E", "E", "Y"], ["E", "E", "Y"], ["E", "R", "Y"],["E", "Y", "Y"], ["E", "R", "Y"], ["Y", "R", "R"]] #vertical matching case 5

        # horizontal matching
        self.tile_types = [["E", "E", "E", "E"], ["E", "E", "E", "Y"], ["E", "E", "E", "Y"], ["E", "E", "R", "R"],
                           ["R", "Y", "Y", "Y"]]  # horizontal matching test 1
        # self.tile_types = [["E", "E", "E", "E"], ["E", "E", "E", "E"],["E", "E", "E", "Y"],["E", "E", "E", "Y"], ["E", "E", "Y", "Y"], ["Y", "Y", "Y", "Y"]] #horizontal matching test 2
        # self.tile_types = [ ["Y", "Y", "Y", "Y", "R", "Y", "Y", "Y" ], ["Y", "Y", "Y", "Y", "R", "R", "Y", "R"]] #horizontal matching test 3

        self.tile_size = 20

        # the reason why we want them to be produced from the same factories is for matching purposes.
        # ex: in DrMario redPill and redVirus should be matchable
        self.falling_tile_types = ["Y", "R"]  # A = yellow pill # B = red pill

    def overriden(f):  # this is just for marking the function as a defined abstract function
        return f

    @overriden
    def set_up_my_game(self):
        self.create_my_tile_board()

    def create_my_tile_board(self):
        self.set_up_my_tile_factories()
        self.set_up_my_falling_tile_factories()
        my_tile_board = DMTileBoard(self.tile_size,
                                    self.factory, self.falling_factory,
                                    self.tile_types, self.falling_tile_types,
                                    2, 2, 3)
        self.set_tile_board(my_tile_board)

    # pre-setup of the tile factory
    def set_up_my_tile_factories(self):
        # create the main factory
        factory = TileAbstractFactory()
        # initialize each inidividual factory
        # yellow_factory = TileFactory(Yellow, Sprite("images/yellow-tile.png"), "Y", False)
        # red_factory = TileFactory(Red, Sprite("images/red-tile.png"), "R", False)
        yellow_factory = TileFactory(Yellow, Sprite("yellow-tile.png"), "Y", False)
        red_factory = TileFactory(Red, Sprite("red-tile.png"), "R", False)

        # register individual factories within the main factory
        factory.register_factory("Y", yellow_factory)
        factory.register_factory("R", red_factory)
        self.set_factory(factory)

    def set_up_my_falling_tile_factories(self):
        falling_factory = TileAbstractFactory()
        # we can take advantage of the sprite, it is still yellow tile
        # but this time it is yellow pill not the virus and since these are different factories there is not conflict between the two
        # yellow_factory = TileFactory(Yellow, Sprite("images/yellow-pill.png"), "A", False)
        # red_factory = TileFactory(Red, Sprite("images/red-pill.png"), "B", False)
        yellow_factory = TileFactory(Yellow, Sprite("yellow-pill.png"), "A", False)
        red_factory = TileFactory(Red, Sprite("red-pill.png"), "B", False)

        falling_factory.register_factory("Y", yellow_factory)
        falling_factory.register_factory("R", red_factory)
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
    #delete these since just for testing purpose only
    myGUI = GUI()
    myDrMarioGame = DrMarioGame(0.08, myGUI)
    myDrMarioGame.run()
