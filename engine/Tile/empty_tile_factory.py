
from Sprite.sprite import Sprite
from Tile.empty_tile import EmptyTile
from Tile.tile import Tile


class EmptyTileFactory:
    def __init__(self):
        self.sprite = "empty-default-tile.png"
        self._instance = None

    def __call__(self) -> Tile:
        if not self._instance:
            self._instance = EmptyTile(self.sprite)
        return self._instance

