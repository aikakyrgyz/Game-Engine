import pygame
from engine.Board.tiles_board import TilesBoard
from engine.Tile.empty_tile import EmptyTile
from engine.Tile.status import Status

class GUI:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Tile Matching Game Environment')

    def draw_board(self, tile_board:TilesBoard):
        self.tile_size = tile_board.get_tile_size()
        
        screen_center_x = self.screen_width // 2
        screen_center_y = self.screen_height // 2
        board_width = tile_board.get_num_columns() * self.tile_size
        board_height = tile_board.get_num_rows() * self.tile_size
        board_left = screen_center_x - (board_width // 2)
        board_top = screen_center_y - (board_height // 2)

        for row in range(0, tile_board.get_num_rows()):
            to_print = ''
            print(f'{row}|', end='')
            for col in range(tile_board.get_num_columns()):
                tile = tile_board.get_tile_on_index(row, col)
                status = tile.get_status()
                letter = tile.get_letter()
                x = col * self.tile_size + board_left
                y = row * self.tile_size + board_top
                if isinstance(tile, EmptyTile):
                    to_print += " " * 3
                    pygame.draw.rect(self.screen, (255, 255, 255), (x, y, self.tile_size, self.tile_size))
                elif status == Status["FALLING"]:
                    to_print += f'[{letter}]'
                    pygame.draw.rect(self.screen, (255, 255, 0), (x, y, self.tile_size, self.tile_size))
                elif status == Status["FALLEN"]:
                    to_print += f'|{letter}|'
                    pygame.draw.rect(self.screen, (255, 255, 0), (x, y, self.tile_size, self.tile_size))
                elif status == Status["MATCHED"]:
                    to_print += f'*{letter}*'
                    pygame.draw.rect(self.screen, (255, 0, 255), (x, y, self.tile_size, self.tile_size))
                else:
                    to_print += " "+ letter + " "
            print(to_print + '|')
        print(f" {3 * tile_board.get_num_columns() * '-' + ' '}")
        pygame.display.update()


    def draw_tile(self, tile):
        #draws tile
        pass
