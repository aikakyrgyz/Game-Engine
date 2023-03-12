import sys
sys.path.append(r'/Users/aigerimkubanychbekova/Desktop/final-women/Inf-122-Final-Project')

from engine.Sprite.sprite import Sprite
from engine.Board.tiles_board import TilesBoard
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
        self.tile_types = [["E", "E", "E"], ["E", "R", "E"], ["Y", "Y", "Y"]]
        self.tile_size = 20
        self.falling_tile_types = ["Y", "R"]  # A = yellow pill # B = red pill

    def set_up_my_game(self):
        self.create_my_tile_board()

    def create_my_tile_board(self):
        self.set_up_my_tile_factories()
        self.set_up_my_falling_tile_factories()
        my_tile_board = TilesBoard(self.tile_size,
                                        self.factory, self.falling_factory,
                                        self.tile_types, self.falling_tile_types,
                                        2, 2)
        self.set_tile_board(my_tile_board)


    def set_up_my_tile_factories(self):
        # create the main factory
        factory = TileAbstractFactory()
        # initialize each inidividual factory
        yellow_factory = TileFactory(Yellow, Sprite("yellow-virus.png"), "Y")
        red_factory = TileFactory(Red, Sprite("red-virus.png"), "R")
        # register individual factories within the main factory
        factory.register_factory("Y", yellow_factory)
        factory.register_factory("R", red_factory)
        self.set_factory(factory)

    def set_up_my_falling_tile_factories(self):
        falling_factory = TileAbstractFactory()
        # we can take advantage of the sprite, it is still yellow tile
        # but this time it is yellow pill not the virus and since these are different factories there is not conflict between the two
        yellow_factory = TileFactory(Yellow, Sprite("yellow-pill.png"), "A")
        red_factory = TileFactory(Red, Sprite("red-pill.png"), "B")
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


myGUI = GUI()
myDrMarioGame = DrMarioGame(60, myGUI)
myDrMarioGame.run()


