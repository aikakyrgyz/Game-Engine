from engine.Board.tiles_board import TilesBoard
from engine.Tile.tileAbstractFactory import TileAbstractFactory
from engine.Tile.status import Status


class DMTileBoard(TilesBoard):
    def __init__(self, tile_size, tile_factories: TileAbstractFactory, falling_tile_factories: TileAbstractFactory, tile_types, falling_tile_types, min_num_tiles, max_num_tiles, min_match_num, min_score, max_score):
        TilesBoard.__init__(self, tile_size, tile_factories, falling_tile_factories, tile_types, falling_tile_types, min_num_tiles, max_num_tiles, min_match_num, min_score, max_score)

    def overriden(f): # for documentation purposes
        return f

    # want to end the game if all the viruses were eliminated

    def viruses_still_present(self):
        for row in range(self.get_num_rows()):
            for col in range(self.get_num_columns()):
                if self.get_tile_on_index(row, col).get_letter() == "Y" or self.get_tile_on_index(row, col).get_letter() == "R":
                    return True
        return False

    @overriden
    def match_all(self):
        # for DR mario we want both matches
        self.horizontal_match()
        self.vertical_match()


    @overriden
    def ending_condition(self) -> bool:
        print("in ending condition")
        # For now the ending condition of the game is when there is at least one tile 
        # filed at the top row of the board. The top row shown in the gui will change
        # depending on how many tiles are falling at once.
        # ex. if 2 tiles are falling -> gui will hide row[0] -> must check row[1] for ending condition
        # ex. if 3 tiles are falling -> gui will hide row[0] and row[1] -> must check row[2] for ending condition
        ## oops, it is supposed to be 2

        topRowOfBoard = self.board[self.max_num_shape_tiles-2]

        # use for testing
        # print("self.max_num_shape_tiles-1", self.max_num_shape_tiles-1)
        # print("topRowOfBoard", topRowOfBoard)

        # if there are still matching tiles present, then it might be possible that it does not end the game,
        # so return False for now

        # we could also do win loss condition
        if self.matched_tiles_present():
            # will see after one more loop
            return False

        if not self.viruses_still_present():
            # this would be a win condition
            print("eliminated all the viruses - game over - WIN!")
            return True

        for tile in topRowOfBoard:
            # this would be loss condition, since the viruses still present
            #use below to test the result of the if statement
            #print(tile.get_letter() != " ", tile.status != Status.FALLING, tile.status != Status.FALLEN)
            # will have to change this something is not working
            if tile.status == Status.STILL:
                print("game over")
                return True
            # if tile.get_letter() != " " and tile.status != Status.FALLING and tile.status != Status.FALLEN and tile.status != Status.MATCHED:
            #     print("game over ")
            #     return True
        
        return False


