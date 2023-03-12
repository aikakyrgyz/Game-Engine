from engine.Board.tiles_board import TilesBoard
from engine.Tile.empty_tile import EmptyTile
from engine.GameObject.status import Status

class GUI:
    def __init__(self):
        pass
    # we can make this class do all the drawing for any object
    # or we can have a draw method in each class, like tile_board

    def draw_board(self, tile_board:TilesBoard):
        for row in range(0, tile_board.get_num_rows()):
            to_print = ''
            print('|', end='')
            for col in range(tile_board.get_num_columns()):
                tile = tile_board.get_tile_on_index(row, col)
                status = tile.get_status()
                letter = tile.get_letter()
                if isinstance(tile, EmptyTile):
                    to_print += " " * 3
                elif status == Status["FALLING"]:
                    to_print += f'[{letter}]'
                elif status == Status["FROZEN"]:
                    to_print += f'|{letter}|'
                elif status == Status["MATCHED"]:
                    to_print += f'*{letter}*'
                else:
                    to_print += " "+ letter + " "
            print(to_print + '|')
        print(f" {3 * tile_board.get_num_columns() * '-' + ' '}")

    def draw_tile(self, tile):
        #draws tile
        pass