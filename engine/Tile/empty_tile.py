from Sprite.sprite import Sprite
from Tile.tile import Tile


class EmptyTile(Tile):
    def __init__(self):
        Tile.__init__(self, Sprite("empty-default-tile.png"))

