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
        # pygame.init()
        # pygame.display.init()
        self.game_outcome = ''
        self._menu = None
        self._start = False
        self.dash = None
        pygame.font.init()  # text added for testing
        self.text_font = pygame.font.SysFont('Arial', 15, False, False)  # text added for testing
        self.screen_width = theme.SURFACE_WIDTH
        self.screen_height = theme.SURFACE_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(apptheme.BACKGROUND_COLOR)
        self.score = 0
        print("Initialized Pygamedisplay")
        pygame.display.set_caption('Tile Matching Game Environment')
        self.theme = theme
        self.in_game_dash()
        pygame.init()

    def draw_board(self, tile_board: TilesBoard):
        self.tile_size = tile_board.get_tile_size() * 3  # multipled for now to increase tile size for visuals
        # clock = pygame.time.Clock() # slows down the tiles

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
                else:
                    to_print += " " + letter + " "
                    self.draw_tile(tile, x, y, self.tile_size)
            print(to_print + '|')
        print(f" {3 * tile_board.get_num_columns() * '-' + ' '}")

        pygame.display.update()
        # clock.tick(3) #slows down the tiles

    # def falling_obj_movement(self, keys_pressed, obj: TilesBoard, velocity=1):
    #     """
    #     Handle the input from the player to move the falling shape
    #     :param keys_pressed: keyboard input from pygame (i.e. keys_pressed = pygame.key.get_pressed())
    #     :param obj: image of a falling shape
    #     :param velocity: speed of the movement, can be adjusted for 'levels'
    #     :return:
    #     """
    #     if obj.get_falling_shape().get_status() == Status.FALLING.value:
    #         if keys_pressed[pygame.K_UP]:
    #             # rotate?
    #             obj.move_falling_shape(ROTATE)
    #         if keys_pressed[pygame.K_DOWN]:
    #             # keep falling
    #             obj.move_falling_shape(DOWN)
    #         if keys_pressed[pygame.K_LEFT]:
    #             # move shape left
    #             obj.move_falling_shape(LEFT)
    #         if keys_pressed[pygame.K_RIGHT]:
    #             obj.move_falling_shape(RIGHT)
    #         return True
    #     return False

    def draw_tile(self, tile: Tile, x, y, tile_size):
        sprite = tile.get_sprite().get_surface()
        sprite = pygame.transform.scale(sprite, (tile_size, tile_size))
        self.screen.blit(sprite, (x, y))


    def update(self, tile_board: TilesBoard, draw_board=True, draw_menu=True):
        if draw_board:
            # Draw the board
            self.draw_board(tile_board)

        if draw_menu:
            self._menu.draw(self.screen)

    def player_start(self, tile_board: TilesBoard):
        while True:
            events = pygame.event.get()
            # self.in_game_dash()
            self._menu.update(events)
            self.update(tile_board)
            pygame.display.flip()

    def in_game_dash(self, score=0):

        self._menu = pygame_menu.Menu(
            title='Dashboard',
            height=self.screen_height/2,
            mouse_motion_selection=True,
            position=(self.screen_width*2/3+50, self.screen_height/4, False),
            width=300,
        )
        # score
        self._menu.add.label(
            f'Current Score {score}',
            font_name=pygame_menu.font.FONT_FIRACODE_BOLD,
            font_size=22,
            margin=(0, 5)
        )
        # start / pause
        self._menu.add.button(
            'Start/Pause',
            button_id='run_game',
            font_size=20,
            margin=(0, 30),
            shadow_width=10,
            action=self.start_game
        )
        # quit game, not app
        self._menu.add.button(
            'Quit',
            button_id='quit_game',
            font_size=20,
            margin=(0, 30),
            shadow_width=10,
            action=pygame_menu.events.CLOSE
        )

    def start_game(self):
        self._start = True
        # self.draw_board(self.tile_board)

    def game_end(self):
        if self.game_outcome == 'win':
            pass
        else:
            # 1P, just display score
            pass

    def player_wins(self, winner):
        # to display the winner of the game
        player_won = pygame_menu.Menu(
            height=self.screen_height,
            width=self.screen_width,
            theme=self.theme.get_theme(),
            title='You win!'
        )
        player_won.add.label(
            f'Player {winner}',
            font_name=apptheme.FONT,
            font_size=50)


if __name__ == '__main__':
    gui = GUI()
    print(LEFT.direction)
