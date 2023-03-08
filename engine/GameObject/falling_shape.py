from abc import abstractmethod

from Board.tiles_board import TilesBoard
from Errors.errors import InvalidIndexError
from GameObject.game_object import GameObject
from GameObject.status import Position, Status
from Tile.tileAbstractFactory import TileAbstractFactory

# later: refractor to a shape factory

class FallingShape(GameObject):
    # to do: try to validate the r, and c without passing tiles_board
    def __init__(self, number_of_tiles:int, tile_types: list[str], tile_factory:TileAbstractFactory, tiles_board: TilesBoard):
        self.status = Status["FALLING"]
        positioon = horizontal
        self.number_of_tiles = number_of_tiles
        self.board = tiles_board
        self.tile_types = tile_types
        self.tile_factory = tile_factory
        self._instance = []
        self.last_tile_index_in_shape = number_of_tiles-1 # remains the same, the index in the shape itself not the board
        # Capsule, tile_types = ["YELLOW", "RED"]
        # the creation shall be in order as specified by the tile_types

        # faller -> |YELLOW|RED| if horizontal

        # rotate -> will change the adjacent tiles

        # faller ->  ______
        #           |YElLOW|
        #            -------
        #           |  RED |   if vertical
        #            -------

        # tile_factory should contain the factories for building the yellow and red tile
        # if horizontal -> row remains unchanged, increment the column as new tiles are appended to the shape
        # if vertical   -> column remains unchanged, increment the row ...

        # create the falling shape
        # we also assume the falling shape is created after the board has been initialized
        # so we want to validate the rows and columns
        # want to create the faller always at the top of the board
        #
        self.createFallingShape()
        self.set_tile_status()

    @abstractmethod
    def create(self):
        pass

    def set_status(self, status: Status):
        self.status = Status.FALLING

    def get_status(self, status):
        return self.status

    def get_tile_on_index_in_falling_shape(self, index):
        # index of the tile in the list, not the index in the board
        if index < 0 or index > self.number_of_tiles:
            raise InvalidIndexError("The index of the faller tile is not valid")
        return self._instance[index]

    def set_tile_status(self):
        for tile in self._instance:
            tile.set_status(Status.FALLING)

    def get_falling_shape(self):
        return self._instance

    def get_position(self) -> Position:
        return self.position

    def set_position(self, position: Position):
        self.position = position

    def rotate(self):
        pass # do we want to rotate

    def get_bottom_tile_row_index(self):
        return self._instance[self.last_tile_index_in_shape].get_row_index()

