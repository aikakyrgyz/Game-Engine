import random
from abc import ABC, abstractmethod

from engine.Errors.errors import InvalidIndexOnBoardError
from engine.GameObject.falling_shape import FallingShape
from engine.GameObject.vertical_falling_shape import VerticalFallingShape
from engine.Tile.empty_tile_factory import EmptyTileFactory
from engine.Tile.tile import Tile
from engine.Tile.empty_tile import EmptyTile
from engine.Tile.tileAbstractFactory import TileAbstractFactory
from engine.GameObject.position import POSITION
from engine.Tile.status import Status


class TilesBoard(ABC):
    def __init__(self, tile_size, tile_factories: TileAbstractFactory, falling_tile_factories: TileAbstractFactory,
                 tile_types, falling_tile_types, min_num_tiles, max_num_tiles, min_match_num):
        self.tile_factories = tile_factories
        self.tile_size = tile_size
        self.falling_tile_factories = falling_tile_factories
        # add the empty tile factory to the tile_factories
        # the client does not have to create an empty factory, it will always have a default image
        self.tile_factories.register_factory("E", EmptyTileFactory())
        # [["EMPTY", "RED", "EMPTY", "EMPTY"],
        #  ["YELLOW", YELLOW", "RED", ....]]
        self.tile_types = tile_types

        # max and min number of tiles for falling shape
        # depending on how the user wants, the number of tiles will be randomly selected within the given range for each shape
        self.max_num_shape_tiles = max_num_tiles
        self.min_num_shape_tiles = min_num_tiles
        
        # the minimum number of tiles for successful matching
        self.min_match_num = min_match_num

        # these are the possible types for the falling shape, ex: yellow pill, red pill /// not virus
        self.falling_tile_types = falling_tile_types

        # create the board using the tile_types
        self.create_board()

        # initially there is no falling shape on the board
        self.falling_shape = None

        # the board will be responsible for issuing game over signal
        self.game_over = False
        
        # this variable is used to control the matching vs. falling shape addition
        self.just_matched = False


    # create the full board with the tiles
    def create_board(self):

        board_rows = []
        # add extra invisible rows on top in order to fit in the falling shape's tile
        # for example if the board size is 5x5 and we have a falling shape with 2 tiles then
        # the falling shape's the most bottom tile would start falling from the 1st row of the tile board
        # making the top tile yet invisible on the board, however we need to fit it somehow on the board 
        # for that reason we will create extra (equal to the number of max_num_tiles in the shape) 
        # empty rows on the top of the board. There is another way to do it, we just keep track of the 
        # yet invisible tiles of the falling shape, however it is harder. 
        for i in range(self.max_num_shape_tiles-1):
            board_columns = []
            for j in range(len(self.tile_types[0])):
                tile = self.tile_factories.create_tile("E")
                tile.set_index(i, j)
                board_columns.append(tile)
            board_rows.append(board_columns)

        # create the actual tile board that is visible
        for i in range(len(self.tile_types)):
            board_columns = []
            for j in range(len(self.tile_types[0])):
                tile = self.tile_factories.create_tile(self.tile_types[i][j])
                tile.set_index(i + self.max_num_shape_tiles, j)
                board_columns.append(tile)
            board_rows.append(board_columns)
        # set the board variable
        self.board = board_rows
        # set the board size
        self.num_rows = len(self.board)
        self.num_cols = len(self.board[0])
        print("Your board is initialized!")
        # print(self.get_tile_on_index(7, 2))
        # self.print_board() - shows the index and types of each cell in the board

    # types_board contains all the initial tile types corresponding to each index 
    # after the board has been initialized, we do not use this variable anymore
    def get_types_board(self):
        return self.tile_types

    # change the tile factory in order to produce different tiles at the same indexes
    def set_tile_factories(self, tile_factories: TileAbstractFactory):
        self.tile_factories = tile_factories
        self.create_board()

    # change the location of types on the board while the tile factories available remain the same
    def set_tile_types(self, types_board: list[str]):
        self.types_board = self.types_board
        self.create_board()

    def get_board_width(self) -> int:
        return len(self.board[0]) * self.tile_factories.get_tile_size()

    def get_board_height(self) -> int:
        return len(self.board) * self.tile_factories.get_tile_size()

    def get_num_columns(self) -> int:
        return self.num_cols

    def get_num_rows(self) -> int:
        return self.num_rows

    # check if the index is not out of boundaries
    def is_valid_location(self, r, c) -> bool:
        if r >= len(self.board) or r < 0 or c > len(self.board[0]) or c < 0:
            return False
        return True

    # changes the current tile object to another tile (used for falling)
    def change_tile(self, r, c, tile: Tile):
        self.board[r][c] = tile

    # set the tile on specific index to an empty tile (used for matching)
    def set_empty_tile(self, r: int, c: int):
        # self.tile_types[r][c] = "E"
        self.board[r][c] = self.tile_factories.create_tile("E")

    def get_tile_type(self, tile: Tile) -> Tile:
        return type(tile)

    def get_tile_type_on_index(self, r: int, c: int) -> str:
        return type(self.board[r][c])
    
    def is_empty_tile(self, r, c) -> bool:
        return isinstance(self.board[r][c], EmptyTile)

    def get_tile_on_index(self, r: int, c: int) -> Tile:
        return self.board[r][c]

    # falling logic 
    
    def get_falling_shape(self) -> FallingShape:
        return self._falling_shape
    
    # decides what position should the next added falling shape have (uncomment when the logic for horizontal shape is done)
    def add_falling_shape(self):
        position = random.choice(POSITION)
        # if position == "VERTICAL":
        self.add_vertical_falling_shape()
        # else:
        # self.add_horizontal_falling_shape()

    def add_vertical_falling_shape(self):
        # randomly select a row to put the falling shape in
        column = random.randint(0, self.num_cols - 1)
        # randomly select the number of tiles this falling shape have
        num_tiles = random.randint(self.min_num_shape_tiles, self.max_num_shape_tiles)
        # create the FallingShape object
        # Note: the most important part we are keeping track in the Falling Shape is the index of its bottom tile on the board.
        shape = FallingShape(POSITION[0], column, num_tiles, self.falling_tile_types, self.falling_tile_factories)
        # retrieve the created falling shape 
        self.falling_shape = shape.get_falling_shape()
        # if the tile on the bottom of the falling shape's bottom tile is empty then the shape can be placed on the board
        if self.is_empty_tile(shape.get_num_tiles() - 1, column):
            # this loop sets all the tiles on the board on which the falling shape is currently put to that shape's tiles
            for i in range(self.max_num_shape_tiles):
                # retrieve the tile of the shape from top -> down 
                shape_tile = shape.get_tile_on_index(i)
                # keep track that this tile contains a piece of the falling shape 
                shape_tile.set_status(Status.FALLING)
                # set the board's tile to the shape's tile
                self.change_tile(i, column, shape_tile)
            self.check_floor()
        else:
            # need to work on ending
            self.game_over = True

    def check_floor(self):
        # checks if the tile below the falling shape is occupied or it is the bottom most tile of the board
        # if it is occupied by another non-empty tile then the falling shape has to land
        landing_row = self.falling_shape.get_bottom_tile_row() + 1
        if landing_row >= self.get_num_rows() or (not self.is_empty_tile(landing_row, self.falling_shape.get_column())):
            # indicate that the falling shape just landed
            self.falling_shape.set_status(Status.FALLEN)
            
            # set all of the tiles of the board to which the falling shape's tile belong to 
            # have the status of already fallen tiles (not falling, not still YET)
            
            # Note: we are setting the tile on BOARD that BELONG to the falling shape
            # We are not changing the faller's tiles' statuses since it is redundant. We can just keep track of the board tiles.
            for i in range(self.falling_shape.get_bottom_tile_row(),
                           self.falling_shape.get_bottom_tile_row() - self.max_num_shape_tiles, -1):
                self.get_tile_on_index(i, self.falling_shape.get_column()).set_status(Status.FALLEN)

    
    def keep_falling(self):
        # increments the faller to fall down
        if self.falling_shape.get_bottom_tile_row() >= self.get_num_rows():
                self.check_floor()
        landing_row = self.falling_shape.get_bottom_tile_row() + 1
        above_row = landing_row - self.max_num_shape_tiles
        if self.is_empty_tile(landing_row, self.falling_shape.get_column()):
            # s is used to retrieve the faller's tiles from bottom -> top
            s = 1
            # increments all of the faller's tiles by one down
            for i in range(landing_row, landing_row - self.max_num_shape_tiles, -1):
                faller_tile = self.falling_shape.get_tile_on_index(self.max_num_shape_tiles - s)
                self.change_tile(i, self.falling_shape.get_column(), faller_tile)
                s += 1
            # since we have incremented all the tiles down, the previous top tile must become empty
            self.change_tile(above_row, self.falling_shape.get_column(), self.tile_factories.create_tile("E"))
            # update the shape's bottom row
            self.falling_shape.fall()
            self.check_floor()

    # def add_vertical_falling_shape(self, falling_shape:FallingShape):
    #     bottom_tile_row_index = falling_shape.get_bottom_tile_row_index()
    #     column_index = falling_shape.get
    #     bottom_tile_index = falling_shape.get_bottom_tile_index()
    #     # if self.get_tile_type_on_index(bottom_tile_index[0], )
    #     # vertical =>  r = (0, num-tiles) ; c = (constant)
    #     # horizontal =>r = (constant) ; c = (column, column + num-tiles)
    #     # for r in range(0, falling_shape.get_num_rows):
    #     #     for c in range()

    def just_landed(self):
        # after the shape just has landed, we can start matching, but first we need to set them as still tiles
        for i in range(self.falling_shape.get_bottom_tile_row(),
                       self.falling_shape.get_bottom_tile_row() - self.max_num_shape_tiles, -1):
            self.get_tile_on_index(i, self.falling_shape.get_column()).set_status(Status.STILL)
        # the faller decomposed to tiles 
        self.faller_disappeared()
        # still need to check if we need to call match all here
        # self.match_all()

    def faller_disappeared(self):
        self.falling_shape = None

    def get_falling_tile_factories(self):
        return self.falling_tile_factories

    def get_falling_tile_types(self):
        return self.falling_tile_types

    def update(self):
        # match only when there is not falling object on the board
        # alternation of shape addition and matching: use just_matched variable
        # this function needs to be made simpler ... match_all should be only called once
        if self.falling_shape is None and not self.just_matched:
            self.clear_out_matches()
            self.fill_holes()
            self.match_all()
            # We want to match before the faller starts falling so alternate match and addition of faller
            self.just_matched = True

        
        if self.falling_shape is not None and self.falling_shape.get_status() == Status.FALLEN:
            self.just_landed()
            self.match_all()


        if self.falling_shape is not None:
            self.keep_falling()
            
        # if there is no faller on the board, add a new one
        elif self.falling_shape is None and self.just_matched:
            self.add_falling_shape()
            self.just_matched = False
    

    def isValidColumn(self):
        # if c == null then the default c will be the center
        if self.col is None:
            c = self.board.get_num_columns() / 2
        elif self.col < 0 or self.col >= len(self.board.get_num_columns()):
            raise InvalidIndexOnBoardError("The column index for the tile is not within the board")

    # for test
    def print_board(self):
        # just to make sure the types and the rows are set accordingly
        for row in self.board:
            for tile in row:
                print(f'[{tile.get_index()}-{type(tile)}]', end='')
            print()

    # starting to implement the matching part

    def horizontal_match(self):
        """Defines the logic for the horizontal match"""
        matched_tiles = []
        for row in range(self.num_rows-1, -1, -1):
            for col in range(self.num_cols):
                tile = self.get_tile_on_index(row, col)
                if len(matched_tiles) == 0:
                    matched_tiles.append(tile)
                    last_matched_index = col
                else:
                    if matched_tiles[-1].matchable(tile) and col - last_matched_index == 1:
                        # match consecutive tiles only: difference == 1
                        matched_tiles.append(tile)
                        last_matched_index += 1
                        # print(matched_tiles[-1].get_letter(), " is matched with ", tile.get_letter())
                    # the column might end as soon as the match reached 3, so it will never come back
                    # need to make sure it is >=
                    if len(matched_tiles) >= self.min_match_num:
                        for t in matched_tiles:
                            # update the score somewhere here?
                            # tile now has a matched status
                            t.set_status(Status.MATCHED)
                        # all have been set to matched
                        # clear out the matched list
                    if not matched_tiles[-1].matchable(tile):
                        matched_tiles = []
                        matched_tiles.append(tile)
                        last_matched_index += 1
            matched_tiles = []

    def clear_out_matches(self):
        # sets all of the matched tiles to empty tiles
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.get_tile_on_index(row, col).get_status() == Status.MATCHED:
                    self.set_empty_tile(row, col)

    def fill_holes(self):
        # after the match, the non-empty "hanging" tiles need to fall down
        # have to go through each row twice since need to move all to the most bottom possible
        for r in range(self.num_rows):
            for row in range(self.num_rows-1):
                for col in range(self.num_cols):
                    # make sure that the tile is not stationary (need to keep it as is)
                    if not self.is_empty_tile(row, col) and not self.is_stationary_tile(row, col) and self.is_empty_tile(row+1, col):
                        # set the bottom tile to this tile
                        self.change_tile(row+1, col, self.get_tile_on_index(row, col))
                        # clear out the current tile
                        self.set_empty_tile(row, col)


    def vertical_match(self):
        """Defines the logic for vertical match"""
        matched_tiles = []
        for col in range(self.num_cols):
            for row in range(self.num_rows-1, -1, -1):
                tile = self.get_tile_on_index(row, col)
                if len(matched_tiles) == 0 :
                    matched_tiles.append(tile)
                    last_matched_index = row 
                else:
                    if matched_tiles[-1].matchable(tile) and last_matched_index - row == 1:
                        # match consecutive tiles only: difference == 1
                        matched_tiles.append(tile)
                        last_matched_index -=1

                    if len(matched_tiles) >= self.min_match_num:
                        for t in matched_tiles:
                            # update the score ?
                            t.set_status(Status.MATCHED)
                        # all have been set to matched
                    if not matched_tiles[-1].matchable(tile):
                        matched_tiles = []
                        matched_tiles.append(tile)
                        last_matched_index -= 1
            matched_tiles = []


    def is_stationary_tile(self, row, col):
        # for example, the virus in Dr.Mario is stationary and it will not fall down even though there is empty space below
        self.get_tile_on_index(row, col).get_stationary()

    @abstractmethod
    def match_all(self):
        """
        Overridden in the child class in order to specify the preferred match
        Can be either:
        horizontal_match()
        vertical_match()
        or both
        """

    pass

    def rotate_shape_on_board(self, shape: FallingShape):
        """ how do we want to turn? to simplify there can be only 1 button to initiate rotation, so there is only
            1 way to rotate. here logic is assuming pivoting on the bottom/left tile location, so if the tiles are
            vertical the top tile will move to be to the right of the bottom tile if the tiles are horizontal,
            the left tile will move 1 row up and the right tile will move to where the left tile was
            * exception: if vertical and against another tile or the right wall, the top tile to move to the bottom
                         tile space, and the bottom tile will move to the cell to the left in the same row.
                           row 1      |top tile||wall|     =>                        |wall|
                           row 2      |bot tile||wall|            |bot tile||top tile||wall|
        """
        # maybe create a method to check a specified neighboring cell?, maybe should be in tiles board?
        # i think tiles_board might need to have the rotate method and this one should be in charge of
        # setting the new x, y coordinates
        if shape.is_falling():              # other option is to get_status & compare to Status.FALLING
            if shape.is_vertical():         # other option is to get_position & compare to Position.VERTICAL
                # check the tile to the right of the bottom tile (col+1),
                # if empty turn the faller - bottom stays (row, col), top is now right (row-1, col+1)

                # if NOT empty follow the exception, check to the left
                # if left tile is empty - bottom is now left (row, col-1), top is now right (row-1, col)

                # if left is NOT empty - cannot rotate
                pass
            elif not shape.is_vertical():    # other option is to get_position & compare to Position.HORIZONTAL
                # check title above the left tile
                # if empty - left becomes top (row+1, col), right tile moves to where left was (row-1, col-1)

                # if NOT empty - does not rotate
                pass



