from abc import ABC

<<<<<<< HEAD
from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile
=======
from Sprite.sprite import Sprite
from Tile.tile import Tile
>>>>>>> c081d3274b5d8dfa7b0a725a3c44ff2f5f121087


class TileFactory:
    def __init__(self, tile_type:Tile, sprite:Sprite):
<<<<<<< HEAD
        self.sprite = sprite
=======
        self.sprite = Sprite
>>>>>>> c081d3274b5d8dfa7b0a725a3c44ff2f5f121087
        self.tile_type = tile_type # class of the tile YellowVirus
        # the client will create this tile_type as a class

    def __call__(self) -> Tile:
        return self.tile_type(self.sprite)

