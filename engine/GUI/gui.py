import pygame
import pygame_menu

from engine.Board.tiles_board import TilesBoard
from engine.GameObject.direction import LEFT, RIGHT, DOWN, ROTATE
from engine.Tile.empty_tile import EmptyTile
from engine.Tile.status import Status
from engine.Sprite.sprite import Sprite
from engine.Tile.tile import Tile
from interface import apptheme


class GUI:
    def __init__(self, theme=apptheme):
        #pygame.init()
        # pygame.display.init()
        pygame.font.init() # text added for testing
        self.text_font = pygame.font.SysFont('Arial', 15, False, False) # text added for testing
        self.screen_width = 1200
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.score = 0
        print("Initialized Pygamedisplay")
        pygame.display.set_caption('Tile Matching Game Environment')
        self.theme = theme
        # pygame.init()
        self.setup_game()
        self.game_display = pygame_menu.Menu(height=self.screen_height,
                                             position=(875, 25, False),
                                             theme=self.theme.get_theme(),
                                             title='',
                                             width=250)

    def draw_board(self, tile_board:TilesBoard):
        self.game_display.add.vertical_margin(10)
        self.game_display.add.label('Select Player',
                                    font_size=22,
                                    margin=(0, 5)
                                    ).translate(-12, 0)
        self.game_display.add.dropselect(title='',
                                         items=[('Player 1', 0),
                                                ('Player 2', 1)],
                                         dropselect_id='player_select',
                                         font_size=16,
                                         padding=0,
                                         placeholder='Select one',
                                         selection_box_height=5,
                                         selection_box_inflate=(0, 20),
                                         selection_box_margin=0,
                                         selection_box_text_margin=10,
                                         selection_box_width=200,
                                         selection_option_font_size=20,
                                         shadow_width=20)
        self.game_display.add.vertical_margin(10)
        start_button = self.game_display.add.button('Start',
                                                    button_id='run_game',
                                                    font_size=20,
                                                    margin=(0, 30),
                                                    shadow_width=10,
                                                    )

    def draw_board(self, tile_board: TilesBoard):
        self.tile_size = tile_board.get_tile_size() * 3  # multipled for now to increase tile size for visuals
        # clock = pygame.time.Clock() # slows down the tiles
        self.tile_size = tile_board.get_tile_size() * 3 # multipled for now to increase tile size for visuals

        screen_center_x = self.screen_width // 2
        screen_center_y = self.screen_height // 2
        board_width = tile_board.get_num_columns() * self.tile_size
        board_height = tile_board.get_num_rows() * self.tile_size
        board_left = screen_center_x - (board_width // 2)
        # board_top = screen_center_y - (board_height // 2)
        board_top = (self.screen_height - board_height) / 2

        for row in range(0, tile_board.get_num_rows()):
            to_print = ''
            print(f'{row}|', end='')
            for col in range(tile_board.get_num_columns()):
                tile = tile_board.get_tile_on_index(row, col)
                status = tile.get_status()
                letter = tile.get_letter()
                # print(f'({row},{col}): {self.tile_size}')
                x = col * self.tile_size + board_left
                y = row * self.tile_size + board_top
                if isinstance(tile, EmptyTile):
                    to_print += " " * 3
                    self.draw_tile(tile, x, y, self.tile_size)
                # elif letter == "R":
                #     to_print += f'[{letter}]'
                #     self.draw_tile(tile, x, y, self.tile_size)
                # elif letter == "Y":
                #     to_print += f'[{letter}]'
                #     self.draw_tile(tile, x, y, self.tile_size)
                elif status == Status["FALLING"]:
                    to_print += f'[{letter}]'
                    self.draw_tile(tile, x, y, self.tile_size)
                    self.draw_tile(tile, x, y, self.tile_size)
                elif status == Status["FALLEN"]:
                    to_print += f'|{letter}|'
                    self.draw_tile(tile, x, y, self.tile_size)
                    self.draw_tile(tile, x, y, self.tile_size)
                elif status == Status["MATCHED"]:
                    to_print += f'*{letter}*'
                    self.draw_tile(tile, x, y, self.tile_size)
                    self.draw_tile(tile, x, y, self.tile_size)                
                else:
                    to_print += " " + letter + " "
                    self.draw_tile(tile, x, y, self.tile_size)
            print(to_print + '|')
        print(f" {3 * tile_board.get_num_columns() * '-' + ' '}")
        pygame.display.update()

    def falling_obj_movement(self, keys_pressed, obj: TilesBoard, velocity=1):
        """
        Handle the input from the player to move the falling shape
        :param keys_pressed: keyboard input from pygame (i.e. keys_pressed = pygame.key.get_pressed())
        :param obj: image of a falling shape
        :param velocity: speed of the movement, can be adjusted for 'levels'
        :return:
        """
        if obj.get_falling_shape().get_status() == Status.FALLING.value:
            if keys_pressed[pygame.K_UP]:
                # rotate?
                obj.move_falling_shape(ROTATE)
            if keys_pressed[pygame.K_DOWN]:
                # keep falling
                obj.move_falling_shape(DOWN)
            if keys_pressed[pygame.K_LEFT]:
                # move shape left
                obj.move_falling_shape(LEFT)
            if keys_pressed[pygame.K_RIGHT]:
                obj.move_falling_shape(RIGHT)
            return True
        return False

    def draw_tile(self, tile: Tile, x, y, tile_size):
        sprite = tile.get_sprite().get_surface()
        sprite = pygame.transform.scale(sprite, (tile_size, tile_size))
        self.screen.blit(sprite, (x, y))

    def setup_game(self):
        theme = apptheme.get_theme()

        self.game_display = pygame_menu.Menu(height=self.screen_height,
                                             position=(875, 25, False),
                                             theme=theme,
                                             title='',
                                             width=250)

        self.game_display.add.vertical_margin(10)
        self.game_display.add.label('Select Player',
                                    font_size=22,
                                    margin=(0, 5)
                                    ).translate(-12, 0)
        self.game_display.add.dropselect(title='',
                                         items=[('Player 1', 0),
                                                ('Player 2', 1)],
                                         dropselect_id='player_select',
                                         font_size=16,
                                         padding=0,
                                         placeholder='Select one',
                                         selection_box_height=5,
                                         selection_box_inflate=(0, 20),
                                         selection_box_margin=0,
                                         selection_box_text_margin=10,
                                         selection_box_width=200,
                                         selection_option_font_size=20,
                                         shadow_width=20)
        self.game_display.add.vertical_margin(10)
        start_button = self.game_display.add.button('Start',
                                                    button_id='run_game',
                                                    font_size=20,
                                                    margin=(0, 30),
                                                    shadow_width=10,
                                                    )



if __name__ == '__main__':
    gui = GUI()
    print(LEFT.direction)
