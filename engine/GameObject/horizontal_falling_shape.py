# from Board.tiles_board import TilesBoard
# from Errors.errors import InvalidIndexError
# from GameObject.falling_shape import FallingShape
# from Tile.tileAbstractFactory import TileAbstractFactory


# class HorizontalFallingShape(FallingShape):

#     def __init__(self, number_of_tiles: int, tile_types: list[str], tile_factory: TileAbstractFactory,
#                  tiles_board: TilesBoard, c):
#         super(number_of_tiles, tile_types, tile_factory, tiles_board)
#         self.isValidCol(c)
#         self.col = c

#     def isValidRow(self):
#         if self.col < 0 or self.col + self.number_of_tiles > len(self.board.get_num_columns()):
#             raise InvalidIndexError("The tile cannot fit within the board with the specified index")
#         @overriden
#     def create(self):
#         for i in range(self.number_of_tiles):
#             tile = self.tile_factory.create_tile(self.tile_types[i])
#             tile.set_index(0, i)
#             self._instance.append(tile)


#     faller = [top_tile, center_tile, bottom_tile]

#     tile = faller.top.getTile()
#     tile = empty

#     tile = faller.middle
#     tile = faller.bottom


#     board.draw


#     faller.draw -> location
#                    r = range(1, 3)
#                     c = constant
#     faller.location (r+1)
#
# def overriden(f):  # this is just for marking the function as a defined abstract function
#     return f