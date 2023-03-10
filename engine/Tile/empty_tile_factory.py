
from Sprite.sprite import Sprite
from Tile.empty_tile import EmptyTile
from Tile.tile import Tile


class EmptyTileFactory:
    def __init__(self):
        self._instance = None

    def __call__(self) -> Tile:
        return EmptyTile()

