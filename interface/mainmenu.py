import os

import pygame
import pygame_menu
import apptheme as app_theme
import registration as reg
from database import game as gamesql
from puyopuyo import puyoui as pm
from drmario import dmUI as dm
import images

PROJ_DIR_IMG = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')


# background image for main menu
def draw_background():
    background_image = pygame_menu.BaseImage(
        # image_path="images/bg_image.jpg"
        image_path=os.path.join(PROJ_DIR_IMG, 'bg_image.jpg')
    )
    background_image.draw(menu.surface)


# move or adjust this function
def get_game_list_menu():
    return gamesql.return_game_list()
    # if no database connection, use the below
    # return [("Dr. Mario", 0, 'mario_image.jpg'), ("Puyo Puyo", 1, 'puyopuyo_image.jpg')]


class MainMenu:
    def __init__(self, title, surface_dimensions, theme=app_theme.get_theme()):
        self.selected_game = get_game_list_menu()[0][0]
        self.players = [pygame_menu.widgets.widget.textinput.TextInput, pygame_menu.widgets.widget.textinput.TextInput]
        self.custom_theme = theme
        self.title = title
        self.surface_height, self.surface_width = surface_dimensions
        self.menu_height = surface_dimensions[0] * 0.75
        self.menu_width = surface_dimensions[1] * 0.75
        self.app_menu = None
        self.selected_game_index = 0

        self.game_modes = {}
        for i in range(len(get_game_list_menu())):
            game = get_game_list_menu()[i][0]
            img_path = get_game_list_menu()[i][2]
            self.game_modes[i] = {
                'image': pygame_menu.BaseImage(image_path=os.path.join(PROJ_DIR_IMG, img_path)).scale(0.15, 0.15),
                'label': {'title': game}
            }

        pygame.init()
        self.surface = pygame.display.set_mode((self.surface_width, self.surface_height))

    def set_title(self, title):
        self.title = title

    # def set_window_dimensions(self, width, height):
    #     self.surface_height = height
    #     self.surface_width = width

    def registration(self):
        player1 = self.players[0].get_value()
        player2 = self.players[1].get_value()

        reg.register_player(player1)
        print(f"Registered Player 1: {player1}")
        # register player 1
        # best to validate here or in registration?
        if player2 != "":
            print(f"Registered Player 2: {player2}")
            reg.register_player(player2)

    def start_selected_game(self):
        """
        register players and start the selected game
        :return:
        """
        # needs some work if we want it to be able to start additional games
        self.registration()
        print("Starting selected game...")
        if self.selected_game_index == 0:
            dm.start_menu()
        elif self.selected_game_index == 1:
            pm.start_menu()
        else:
            print("Mo game selected!")

    def update_game_from_selection(self):
        """
        changes image & play button based on user selection
        :return:
        """
        self.image_widget.set_image(self.game_modes[self.selected_game_index]['image'])
        self.play_button.set_title('Play ' + self.game_modes[self.selected_game_index]['label']['title'])

    def start_menu(self):

        def set_game(*args):
            self.selected_game_index = self.app_menu.get_widget('select_game').get_index()
            # self.selected_game = self.app_menu.get_widget('select_game').get_attribute()
            self.selected_game = get_game_list_menu()[self.selected_game_index][0]
            print(f"Selected Game: {self.selected_game}")
            self.update_game_from_selection()

        #
        reg_menu = pygame_menu.Menu(
            height=self.menu_height,
            width=self.menu_width,
            theme=self.custom_theme,
            title='Register Players'
        )


        # # game image example. needs a lot of work
        # if self.selected_game_index == 0:
        #     # game_image = "images/mario_image.jpg"
        #     game_image = os.path.join(PROJ_DIR_IMG, 'mario_image.jpg')
        #     # print(os.path.join(PROJ_DIR_IMG, 'mario_image.jpg'))
        # else:
        #     game_image = "images/puyopuyo_image.jpg"
        #     game_image = os.path.join(PROJ_DIR_IMG, 'puyopuyo_image.jpg')

        self.players[0] = reg_menu.add.text_input('Player 1: ', input_underline_hmargin=5) \
            .set_margin(400, 0).set_alignment(pygame_menu.locals.ALIGN_LEFT, )

        self.players[1] = reg_menu.add.text_input('Player 2: ', default="") \
            .set_margin(400, 0).set_alignment(pygame_menu.locals.ALIGN_LEFT, )

        self.image_widget = reg_menu.add.image(
            image_path=self.game_modes[self.selected_game_index]['image'],
            padding=(25, 0, 0, 0),  # top, right, bottom, left
            scale=(0.15, 0.15),
            align=pygame_menu.locals.ALIGN_LEFT,
            set_margin=(400, 400)
        )

        self.play_button = reg_menu.add.button(f'Play', self.start_selected_game)
        # self.play1 = reg_menu.add.button(f'Play {get_game_list_menu()[1][0]}', self.start_selected_game)

        back_btn = reg_menu.add.button('Back', pygame_menu.events.BACK)
        quit_btn = reg_menu.add.button('Quit', pygame_menu.events.EXIT)

        # menu widget alignment
        self.players[0].translate(0, 90)
        self.players[1].translate(0, 90)
        # move image off of left margin
        self.image_widget.translate(50, -120)
        self.play_button.translate(0, -80)
        back_btn.translate(-75, -70)
        quit_btn.translate(75, -146)


        pygame.display.set_caption(self.title)
        self.app_menu = pygame_menu.Menu(height=self.menu_height,
                                         width=self.menu_width,
                                         theme=self.custom_theme,
                                         title='Main Menu'
                                         )

        # self.display_mainmenu_items(infont)
        self.app_menu.add.selector(title='Select Game ',
                                   items=get_game_list_menu(),
                                   onchange=set_game,
                                   selector_id='select_game'
                                   )
        self.app_menu.add.button('Play', reg_menu)
        self.app_menu.add.button('Quit', pygame_menu.events.EXIT)


if __name__ == '__main__':
    menu = MainMenu(app_theme.APP_TITLE, (app_theme.SURFACE_HEIGHT, app_theme.SURFACE_WIDTH), app_theme.get_theme())
    # menu.set_title(app_theme.APP_TITLE)
    menu.start_menu()
    menu.app_menu.mainloop(menu.surface, bgfun=draw_background)
