
from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile


class EmptyTile(Tile):
    def __init__(self):
        self.sprite = Sprite("empty-default-tile.png");
        Tile.__init__(self, self.sprite, ' ')

