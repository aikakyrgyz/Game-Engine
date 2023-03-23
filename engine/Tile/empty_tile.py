import os

from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile

IMG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'images')


class EmptyTile(Tile):
    def __init__(self):
        # self.sprite = Sprite("images_/empty-default-tile.png"); AS A JOKE
        self.sprite = Sprite("empty-default-tile.jpg");

        Tile.__init__(self, self.sprite, ' ', False)

