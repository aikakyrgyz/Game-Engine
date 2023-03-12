from abc import abstractmethod

# later: refractor to a shape factory
from engine.Errors.errors import InvalidIndexOnBoardError
from engine.GameObject.game_object import GameObject
from engine.GameObject.status import Status, Position
from engine.Tile.tileAbstractFactory import TileAbstractFactory


# later: refractor to a shape factory

class FallingShape(GameObject):
    # to do: try to validate the r, and c without passing tiles_board
    def __init__(self, column, number_of_tiles: int, tile_types: list[str], tile_factories:TileAbstractFactory):
        self.status = Status["FALLING"]
        self.column = column
        self.number_of_tiles = number_of_tiles
        self.tile_types = tile_types
        self.factory = tile_factories
        self._instance = []
        self.bottom_tile_row = 0
        # self.set_tile_status()
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


    @abstractmethod
    def create(self):
        """Overridden by our horizontal and vertical shapes, since the creation for both differs"""
        pass

    def set_status(self, status: Status):
        self.status = status

    def get_status(self, status: Status):
        return self.status

    def get_column(self):
        return self.column

    def get_tile_on_index_in_falling_shape(self, index):
        # index of the tile in the list, not the index in the board
        if index < 0 or index > self.number_of_tiles:
            raise InvalidIndexOnBoardError("The index of the faller tile is not valid")
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

    def get_bottom_tile_row(self):
        return self.bottom_tile_row

    def get_bottom_tile_row_index(self):
        return self._instance[self.last_tile_index_in_shape].get_row_index()

