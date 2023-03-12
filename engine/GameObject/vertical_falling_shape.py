import random
from engine.Errors.errors import InvalidIndexOnBoardError
from engine.Errors.errors import TileFactoryDoesNotExist
from engine.GameObject.falling_shape import FallingShape
from engine.Tile.tileAbstractFactory import TileAbstractFactory


class VerticalFallingShape(FallingShape):
    def __init__(self, column, number_of_tiles:int, tile_types: list[str], tile_factory:TileAbstractFactory):
        FallingShape.__init__(self, column, number_of_tiles, tile_types, tile_factory)
        self.create()

    def overriden(f): # for documentation purposes
        return f

    def get_falling_shape(self):
        return self._instance

    def get_bottom_tile_row(self):
        return self._instance[-1].get_row_index()

    def move_down(self):
        self.bottom_tile_row += 1

    @overriden
    def create(self):
        for tile in range(0, self.number_of_tiles):
            tile_type = random.choice(self.tile_types)
            tile = self.factory.create_tile(tile_type)
            tile.set_index(tile, self.get_column())
            self._instance.append(tile)
        print("The faller has been created")
        print([tile.get_letter() for tile in self._instance])

    def _require_valid_factories(self):
            for type in self.tile_types:
                if self.factory.get(type) == None:
                    raise TileFactoryDoesNotExist(f"The tile factory for type {type} does not exist")



