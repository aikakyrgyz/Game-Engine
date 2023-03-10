<<<<<<< HEAD
from engine.Tile.empty_tile import EmptyTile
from engine.Tile.tile import Tile
=======

from Sprite.sprite import Sprite
from Tile.empty_tile import EmptyTile
from Tile.tile import Tile
>>>>>>> c081d3274b5d8dfa7b0a725a3c44ff2f5f121087


class EmptyTileFactory:
    def __init__(self):
        self._instance = None

    def __call__(self) -> Tile:
        return EmptyTile()

