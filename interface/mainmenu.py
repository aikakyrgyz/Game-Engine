import pygame
import pygame_menu
import apptheme as app_theme
import registration as reg
from puyopuyo import puyoui as pm
from drmario import drmui as dm


# move or adjust this function
def get_game_list_menu():
    """
    gets the list of games currently in the system
    :return:
    """
    # maybe get this from the server?
    return [("Dr. Mario", 0), ("Puyo Puyo", 1)]


class MainMenu:
    def __init__(self, title, surface_dimensions, theme=pygame_menu.themes.THEME_DARK):
        self.selected_game = get_game_list_menu()[0][0]
        self.players = [pygame_menu.widgets.widget.textinput.TextInput, pygame_menu.widgets.widget.textinput.TextInput]
        self.custom_theme = theme
        self.title = title
        self.surface_height, self.surface_width = surface_dimensions
        self.menu_height = surface_dimensions[0] * 0.75
        self.menu_width = surface_dimensions[1] * 0.75
        self.app_menu = None
        self.selected_game_index = 0

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

        print(f"register player 1: {player1}")
        # register player 1
        reg.register_player(player1)
        # best to validate here or in registration?
        if player2 != "":
            print(f"register player 2: {player2}")
            reg.register_player(player2)

    def start_selected_game(self):
        self.registration()
        print("starting selected game...")
        if self.selected_game_index == 0:
            dm.start_menu()
        elif self.selected_game_index == 1:
            pm.start_menu()
        else:
            print("no game selected")

    def start_menu(self):

        def set_game(*args):
            self.selected_game_index = self.app_menu.get_widget('select_game').get_index()
            # self.selected_game = self.app_menu.get_widget('select_game').get_attribute()
            self.selected_game = get_game_list_menu()[self.selected_game_index][0]
            print(f"selected game: {self.selected_game}")

        #
        reg_menu = pygame_menu.Menu(
            height=self.menu_height,
            width=self.menu_width,
            theme=self.custom_theme,
            title='Register Players'
        )

        self.players[0] = reg_menu.add.text_input('Player 1: ', input_underline_hmargin=5)\
            .set_margin(400, 0).set_alignment(pygame_menu.locals.ALIGN_LEFT,)
        self.players[1] = reg_menu.add.text_input('Player 2: ', default="")\
            .set_margin(400, 0).set_alignment(pygame_menu.locals.ALIGN_LEFT,)
        reg_menu.add.button(f'Play {get_game_list_menu()[self.selected_game_index][0]}', self.start_selected_game)
        reg_menu.add.button('Back', pygame_menu.events.BACK)
        reg_menu.add.button('Quit', pygame_menu.events.EXIT)

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
    menu.app_menu.mainloop(menu.surface)
