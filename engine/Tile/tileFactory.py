from abc import ABC

from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile


class TileFactory:
    def __init__(self, tile_type:Tile, sprite:Sprite):
        self.sprite = sprite
        self.tile_type = tile_type # class of the tile YellowVirus
        # the client will create this tile_type as a class

    def __call__(self) -> Tile:
        return self.tile_type(self.sprite)

