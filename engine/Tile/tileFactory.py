from abc import ABC

from Sprite.sprite import Sprite
from Tile.tile import Tile


class TileFactory:
    def __init__(self, tile_type:Tile, sprite:Sprite):
        self.sprite = Sprite
        self.tile_type = tile_type # class of the tile YellowVirus
        # the client will create this tile_type as a class
        self._instance = None

    def __call__(self) -> Tile:
        if not self._instance:
            self._instance = self.tile_type(self.sprite)
            # calling the constructor of that type
        return self._instance

