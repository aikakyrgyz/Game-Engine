<<<<<<< HEAD
from engine.GameObject.status import Status
from engine.Sprite.sprite import Sprite

=======
from Sprite.sprite import Sprite
from GameObject.status import Status
>>>>>>> c081d3274b5d8dfa7b0a725a3c44ff2f5f121087

class Tile:
    def __init__(self, sprite:Sprite):
        self.sprite = sprite
        self.matchable = True

    def get_sprite(self):
        return self.sprite

    def set_sprite(self, sprite):
        self.sprite = sprite

    def set_sprite_size(self, w):
        self.sprite.set_size(w)

    def set_index(self, r, c):
        self.row, self.col = r, c

    def get_index(self):
        return (self.row, self.col)

    def get_row_index(self):
        return self.row

    def get_col_index(self):
        return self.col
<<<<<<< HEAD


=======
>>>>>>> c081d3274b5d8dfa7b0a725a3c44ff2f5f121087
    def set_status(self, status: Status):
        self.status = status

    def set_matchable(self, m: bool):
        self.matchable = m

