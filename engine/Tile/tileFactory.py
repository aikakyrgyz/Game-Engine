from abc import ABC

from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile

class TileFactory:
    def __init__(self, tile_type:Tile, sprite:Sprite, letter: str):
        self.tile_type = tile_type
        self.sprite = sprite
        self.letter = letter

    def __call__(self) -> Tile:
        return self.tile_type(self.sprite, self.letter)

