<<<<<<< HEAD
from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile
=======
from Sprite.sprite import Sprite
from Tile.tile import Tile
>>>>>>> c081d3274b5d8dfa7b0a725a3c44ff2f5f121087


class EmptyTile(Tile):
    def __init__(self):
        Tile.__init__(self, Sprite("empty-default-tile.png"))

