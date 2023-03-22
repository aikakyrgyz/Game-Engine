
from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile


class EmptyTile(Tile):
    def __init__(self):
        # self.sprite = Sprite("/Users/aigerimkubanychbekova/Desktop/final-women/Inf-122-Final-Project/images/empty-default-tile.jpg")
        self.sprite = Sprite("images/empty-default-tile.jpg")

        Tile.__init__(self, self.sprite, ' ', False)

