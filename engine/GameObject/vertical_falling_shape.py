# from Board.tiles_board import TilesBoard
# from Errors.errors import InvalidIndexError
# from GameObject.falling_shape import FallingShape
# from Tile.tileAbstractFactory import TileAbstractFactory


# class VerticalFallingShape(FallingShape):
#     def __init__(self, number_of_tiles:int, tile_types: list[str], tile_factory:TileAbstractFactory, tiles_board: TilesBoard, c):
#         super(number_of_tiles, tile_types, tile_factory, tiles_board)
#         self.isValidColumn(c)
#         self.col = c

#     def create(self):
#         center = self.number_of_tiles/2
#         for i in range(self.number_of_tiles):
#             tile = self.tile_factory.create_tile(self.tile_types[i])
#             if i == center:
#                 self.center = (i, self.c)
#             tile.set_index(i, self.c)
#             self._instance.append(tile)

#         #
#         # [L, R]
#         # [T]
#         #
#         # [L, R]
#         # [L]
#         #
#         #     [R]
#         #

#         # [1, 2, 3, 4]
#         # [1, 2]


#     def isValidColumn(self):
#         # if c == null then the default c will be the center
#         if self.col is None:
#             c = self.board.get_num_columns() / 2
#         elif  self.col < 0 or self.col >= len(self.board.get_num_columns()):
#             raise InvalidIndexError("The column index for the tile is not within the board")

