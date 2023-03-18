from engine.Tile.empty_tile import EmptyTile
from engine.Tile.tile import Tile


class EmptyTileFactory:
    def __call__(self) -> Tile:
        return EmptyTile()

