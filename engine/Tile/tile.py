
from engine.GameObject.status import Status
from engine.Sprite.sprite import Sprite


class Tile:
    def __init__(self, sprite:Sprite, letter):
        self.sprite = sprite
        self.matchable = True
        self.letter = letter
        self.status = None

    def get_sprite(self):
        return self.sprite

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_letter(self):
        return self.letter

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

    def set_status(self, status: Status):
        self.status = status

    def set_matchable(self, m: bool):
        self.matchable = m

