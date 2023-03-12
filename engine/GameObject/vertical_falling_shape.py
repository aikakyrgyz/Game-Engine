
import random
from engine.Errors.errors import InvalidIndexOnBoardError
from engine.Errors.errors import TileFactoryDoesNotExist
from engine.GameObject.falling_shape import FallingShape
from engine.Tile.tileAbstractFactory import TileAbstractFactory


class VerticalFallingShape(FallingShape):
    def __init__(self, column, number_of_tiles:int, tile_types: list[str], tile_factory:TileAbstractFactory):
        FallingShape.__init__(self, column, number_of_tiles, tile_types, tile_factory)
        self.create()

    def get_falling_shape(self):
        return self._instance

    def get_bottom_tile_row(self):
        return self._instance[-1].get_row_index()

    def move_down(self):
        self.bottom_tile_row += 1

    def create(self):
        for tile in range(0, self.number_of_tiles):
            tile_type = random.choice(self.tile_types)
            tile = self.factory.create_tile(tile_type)
            tile.set_index(tile, self.get_column())
            self._instance.append(tile)
        print("The faller has been created")
        print([tile.get_letter() for tile in self._instance])
        # center = self.number_of_tiles/2
        # for i in range(self.number_of_tiles):
        #     tile = self.tile_factory.create_tile(self.tile_types[i])
        #     if i == center:
        #         self.center = (i, self.c)
        #     tile.set_index(i, self.c)
        #     self._instance.append(tile)

    def _require_valid_factories(self):
            for type in self.tile_types:
                if self.factory.get(type) == None:
                    raise TileFactoryDoesNotExist(f"The tile factory for type {type} does not exist")

    def isValidColumn(self):
        # if c == null then the default c will be the center
        if self.col is None:
            c = self.board.get_num_columns() / 2
        elif  self.col < 0 or self.col >= len(self.board.get_num_columns()):
            raise InvalidIndexOnBoardError("The column index for the tile is not within the board")

