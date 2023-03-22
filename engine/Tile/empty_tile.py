
from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile


class EmptyTile(Tile):
    def __init__(self):
        # self.sprite = Sprite("images/empty-default-tile.png"); AS A JOKE
        self.sprite = Sprite("images/empty-default-tile.jpg")
        Tile.__init__(self, self.sprite, ' ', False)

