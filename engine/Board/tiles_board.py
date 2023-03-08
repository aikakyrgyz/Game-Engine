from GameObject.falling_shape import FallingShape
from GameObject.status import Position
from Tile.empty_tile_factory import EmptyTileFactory
from Tile.tile import Tile
from Tile.tileAbstractFactory import TileAbstractFactory


class TilesBoard:
    # def __init__(self):
    #     # can the sprint already have a size?
    #     # maybe we just assume the tile size is the same as the sprite.
    #     self.tile_size = self.tile_size

    def __init__(self, tile_size, tile_factories: TileAbstractFactory, types_board: list[str][str]):
        self.tile_factories = tile_factories
        self.tile_size = tile_size;
        # add the empty tile factory to the tile_factories
        # the client does not have to create an empty factory, it will always have a default image
        self.tile_factories.register_factory("EMPTY", EmptyTileFactory())
        # {{"EMPTY", "RED", "EMPTY", "EMPTY"}
        #  {"YELLOW", YELLOW", "RED", ....}
        self.types_board = types_board
        self.create_board()
        self.falling_shape = None
        self.game_over = False


    # create the full board with the tiles
    def create_board(self):
        board_rows = []
        for i in range(len(self.types_board)):
            board_columns = []
            for j in range(len(self.types_board[0])):
                tile = self.tile_factories.create_tile(self.types_board[i][j])
                tile.set_index(i, j)
                board_columns.append(tile)
            board_rows.append(board_columns)
        self.board = board_rows
        # set the board size
        self.rows = len(self.board)
        self.cols = len(self.board[0])

    # types_board contains all the tile types corresponding to each index in the index
    def get_types_board(self):
        return self.types_board

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
        return self.cols

    def get_num_rows(self) -> int:
        return self.rows

    # check if the index is not out of boundaries
    def is_valid_location(self, r, c)-> bool:
        if r>=len(self.board) or r<0 or c>len(self.board[0]) or c<0:
            return False
        return True

    # change the type of the Tile at [r, c], the type must be the exsiting type in the tile factory
    def set_tile(self, r: int, c: int, type: str):
        if self.is_valid_location(r, c):
            self.types_board[r][c] = type
            self.board[r][c] = self.tile_factories.create_tile(type)

    def set_empty_tile(self, r:int, c:int):
        self.types_board[r][c] = "EMPTY"
        self.board[r][c] = self.tile_factories.create_tile("EMPTY")

    def get_tile_type(self, tile:Tile) -> Tile:
        return type(tile)

    def get_tile_type_on_index(self, r:int, c: int) -> str:
        return self.types_board[r][c]

    def get_tile_on_index(self, r: int, c: int) -> Tile:
        return self.board[r][c]

    # starting to implement the matching part

    def get_falling_shape(self) -> FallingShape:
        return self.falling_shape


    def add_falling_shape(self, falling_shape: FallingShape):
        self.falling_shape = falling_shape
        falling_shape_position = falling_shape.get_position()
        if falling_shape_position == Position.VERTICAL:
            self.add_vertical_falling_shape(falling_shape)

    def add_vertical_falling_shape(self, falling_shape:FallingShape):
        bottom_tile_row_index = falling_shape.get_bottom_tile_row_index()
        column_index = falling_shape.get
        bottom_tile_index = falling_shape.get_bottom_tile_index()
        # if self.get_tile_type_on_index(bottom_tile_index[0], )
        # vertical =>  r = (0, num-tiles) ; c = (constant)
        # horizontal =>r = (constant) ; c = (column, column + num-tiles)
        # for r in range(0, falling_shape.get_num_rows):
        #     for c in range()




    def update(self):
        # 1. check if the falling shape will be fine falling farther
        # 2. call fallingShape.update of its own
        pass










