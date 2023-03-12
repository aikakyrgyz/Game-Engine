
import random

from engine.GameObject.falling_shape import FallingShape
from engine.GameObject.status import Position
from engine.GameObject.vertical_falling_shape import VerticalFallingShape
from engine.Tile.empty_tile_factory import EmptyTileFactory
from engine.Tile.tile import Tile
from engine.Tile.tileAbstractFactory import TileAbstractFactory


class TilesBoard:
    def __init__(self, tile_size, tile_factories: TileAbstractFactory, falling_tile_factories: TileAbstractFactory, tile_types, falling_tile_types, min_num_tiles, max_num_tiles):
        self.tile_factories = tile_factories
        self.tile_size = tile_size
        self.falling_tile_factories = falling_tile_factories
        # add the empty tile factory to the tile_factories
        # the client does not have to create an empty factory, it will always have a default image
        self.tile_factories.register_factory("E", EmptyTileFactory())
        # [["EMPTY", "RED", "EMPTY", "EMPTY"],
        #  ["YELLOW", YELLOW", "RED", ....]]
        self.tile_types = tile_types

        # max number of tiles for falling shape
        self.max_num_shape_tiles = max_num_tiles
        self.min_num_shape_tiles = min_num_tiles

        # these are the possible types for the falling shape, ex: yellow pill, red pill /// not virus
        self.falling_tile_types = falling_tile_types

        # create the board using the tile_types
        self.create_board()

        # initially there is no falling shape on the board
        self.falling_shape = None

        # the board will be responsible for issuing game over signal
        self.game_over = False

    # create the full board with the tiles
    def create_board(self):
        board_rows = []
        for i in range(len(self.tile_types)):
            board_columns = []
            for j in range(len(self.tile_types[0])):
                tile = self.tile_factories.create_tile(self.tile_types[i][j])
                tile.set_index(i, j)
                board_columns.append(tile)
            board_rows.append(board_columns)
        self.board = board_rows
        # set the board size
        self.num_rows = len(self.board)
        self.num_cols = len(self.board[0])
        print("Your board is initialized!")
        self.print_board()

    # types_board contains all the tile types corresponding to each index in the index
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

    def draw_board(self):
        pass

    def get_board_width(self) -> int:
        return len(self.board[0]) * self.tile_factories.get_tile_size()

    def get_board_height(self) -> int:
        return len(self.board) * self.tile_factories.get_tile_size()

    def get_num_columns(self) -> int:
        return self.num_cols

    def get_num_rows(self) -> int:
        return self.num_rows

    # check if the index is not out of boundaries
    def is_valid_location(self, r, c)-> bool:
        if r>=len(self.board) or r<0 or c>len(self.board[0]) or c<0:
            return False
        return True

    # change the type of the Tile at [r, c], the type must be the exsiting type in the tile factory
    def set_tile(self, r: int, c: int, type: str):
        if self.is_valid_location(r, c):
            self.tile_types[r][c] = type
            self.board[r][c] = self.tile_factories.create_tile(type)

    def set_empty_tile(self, r:int, c:int):
        self.tile_types[r][c] = "EMPTY"
        self.board[r][c] = self.tile_factories.create_tile("EMPTY")

    def get_tile_type(self, tile:Tile) -> Tile:
        return type(tile)

    def get_tile_type_on_index(self, r:int, c: int) -> str:
        return self.tile_types[r][c]

    def get_tile_on_index(self, r: int, c: int) -> Tile:
        return self.board[r][c]

    # starting to implement the matching part

    def get_falling_shape(self) -> FallingShape:
        return self._falling_shape

    def add_falling_shape(self):
        self.add_vertical_falling_shape()

    # def add_vertical_falling_shape(self, falling_shape:FallingShape):
    #     bottom_tile_row_index = falling_shape.get_bottom_tile_row_index()
    #     column_index = falling_shape.get
    #     bottom_tile_index = falling_shape.get_bottom_tile_index()
    #     # if self.get_tile_type_on_index(bottom_tile_index[0], )
    #     # vertical =>  r = (0, num-tiles) ; c = (constant)
    #     # horizontal =>r = (constant) ; c = (column, column + num-tiles)
    #     # for r in range(0, falling_shape.get_num_rows):
    #     #     for c in range()

    def get_falling_tile_factories(self):
        return self.falling_tile_factories

    def get_falling_tile_types(self):
        return self.falling_tile_types

    def add_vertical_falling_shape(self):
        column = random.randint(0, self.num_cols-1)
        num_tiles = random.randint(self.min_num_shape_tiles, self.max_num_shape_tiles)
        shape = VerticalFallingShape(column, num_tiles, self.falling_tile_types, self.falling_tile_factories)
        self.falling_shape = shape.get_falling_shape()

    def update(self):
        # 1. check if the falling shape will be fine falling farther
        # 2. call fallingShape.update of its own
        pass


  # for test
    def print_board(self):
        for row in self.board:
            for tile in row:
                print(f'[{tile.get_index()}-{type(tile)}]', end = '')
            print()








