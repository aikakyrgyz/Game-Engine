from abc import abstractmethod
import random
# later: refractor to a shape factory
from engine.Errors.errors import InvalidIndexOnBoardError, TileFactoryDoesNotExist
from engine.GameObject.game_object import GameObject
from engine.Tile.tileAbstractFactory import TileAbstractFactory
from engine.Tile.status import Status

# later: refractor to a shape factory

class FallingShape(GameObject):
    # to do: try to validate the r, and c without passing tiles_board
    def __init__(self, position, column, number_of_tiles: int, tile_types: list[str], tile_factories:TileAbstractFactory):
        self.status = Status["FALLING"]
        self.column = column
        self.number_of_tiles = number_of_tiles
        self.tile_types = tile_types
        self.factory = tile_factories
        self._instance = []
        self.bottom_tile_row = number_of_tiles-1
        self.position = position
        self.create()
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


    # @abstractmethod
    # def create(self):
    #     """Overridden by our horizontal and vertical shapes, since the creation for both differs"""
    #     pass

    def create(self):
        for i in range(0, self.number_of_tiles):
            tile_type = random.choice(self.tile_types)
            tile = self.factory.create_tile(tile_type)
            tile.set_status(Status.FALLING)
            tile.set_index(i, self.get_column())
            self._instance.append(tile)
        print("The faller has been created")
        print([tile.get_letter() for tile in self._instance])

    def update(self):
        """Override how each faller updates"""
        pass

    def set_status(self, status: Status):
        self.status = status

    def get_status(self):
        return self.status

    def get_column(self):
        return self.column

    def get_tile_on_index(self, index):
        # index of the tile in the list, not the index in the board
        if index < 0 or index > self.number_of_tiles:
            raise InvalidIndexOnBoardError("The index of the faller tile is not valid")
        return self._instance[index]

    def set_tile_status(self):
        for tile in self._instance:
            tile.set_status(Status.FALLING)

    def get_num_tiles(self):
        return self.number_of_tiles

    def get_falling_shape(self):
        return self

    def rotate(self):
        pass # do we want to rotate

    def fall(self):
        self.bottom_tile_row+=1

    def get_bottom_tile_row(self):
        return self.bottom_tile_row

    def get_bottom_tile_row_index(self):
        return self._instance[self.last_tile_index_in_shape].get_row_index()

    def _require_valid_factories(self):
            for type in self.tile_types:
                if self.factory.get(type) == None:
                    raise TileFactoryDoesNotExist(f"The tile factory for type {type} does not exist")



    def change_coordinates(self):
        """
        must update coordinates of all tiles in the shape
        """
        pass
