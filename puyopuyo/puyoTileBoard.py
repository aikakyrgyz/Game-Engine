from engine.Board.tiles_board import TilesBoard
from engine.Tile.tileAbstractFactory import TileAbstractFactory


class PuyoTileBoard(TilesBoard):
    def __init__(self, tile_size, tile_factories: TileAbstractFactory, falling_tile_factories: TileAbstractFactory, tile_types, falling_tile_types, min_num_tiles, max_num_tiles, min_match_num):
        TilesBoard.__init__(self, tile_size, tile_factories, falling_tile_factories, tile_types, falling_tile_types, min_num_tiles, max_num_tiles, min_match_num)

    def overriden(f): # for documentation purposes
        return f

    @overriden
    def match_all(self):
        # for Puyopuyo we want group matches
        self.group_match()
        
        # to test
        # self.vertical_match()
        # self.horizontal_match()
    
    @overriden
    def ending_condition(self) -> bool:
        # for now the ending condition of the game is when there is at least one tile 
        # filed at the top row of the board
        topRowOfBoard = self.board[0]

        for tile in topRowOfBoard:
            if tile.get_letter() != "E":
                return False
        
        return True

