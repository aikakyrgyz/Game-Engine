from engine.Board.tiles_board import TilesBoard
from engine.Tile.tileAbstractFactory import TileAbstractFactory
from engine.Tile.status import Status


class DMTileBoard(TilesBoard):
    def __init__(self, tile_size, tile_factories: TileAbstractFactory, falling_tile_factories: TileAbstractFactory, tile_types, falling_tile_types, min_num_tiles, max_num_tiles, min_match_num):
        TilesBoard.__init__(self, tile_size, tile_factories, falling_tile_factories, tile_types, falling_tile_types, min_num_tiles, max_num_tiles, min_match_num)

    def overriden(f): # for documentation purposes
        return f

    @overriden
    def match_all(self):
        # for DR mario we want both matches
        self.horizontal_match()
        #self.group_match()
        self.vertical_match()

    @overriden
    def ending_condition(self) -> bool:
        # For now the ending condition of the game is when there is at least one tile 
        # filed at the top row of the board. The top row shown in the gui will change
        # depending on how many tiles are falling at once.
        # ex. if 2 tiles are falling -> gui will hide row[0] -> must check row[1] for ending condition
        # ex. if 3 tiles are falling -> gui will hide row[0] and row[1] -> must check row[2] for ending condition
        topRowOfBoard = self.board[self.max_num_shape_tiles-1]

        # use for testing
        # print("self.max_num_shape_tiles-1", self.max_num_shape_tiles-1)
        # print("topRowOfBoard", topRowOfBoard)

        for tile in topRowOfBoard:
            #use below to test the result of the if statement
            #print(tile.get_letter() != " ", tile.status != Status.FALLING, tile.status != Status.FALLEN)
            if tile.get_letter() != " " and tile.status != Status.FALLING and tile.status != Status.FALLEN:
                print("game over")
                return True
        
        return False
