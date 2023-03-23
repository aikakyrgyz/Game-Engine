import os
import pygame
import pygame_menu
import apptheme as app_theme
import registration as reg
import profile
import scoreboard as score
from database import player
from puyopuyo import puyoui as pm
from drmario import dmUI as dm

PROJ_DIR_IMG = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')


# background image for main menu
def draw_background():
    background_image = pygame_menu.BaseImage(
        # image_path="images_/bg_image.jpg"
        image_path=os.path.join(PROJ_DIR_IMG, 'bg_image.jpg')
    )
    background_image.draw(menu.surface)


# move or adjust this function
def get_game_list_menu():
    # return gamesql.return_game_list()
    # if no database connection, use the below
    return [("Dr. Mario", 0, 'mario_image.jpg'), ("Puyo Puyo", 1, 'puyopuyo_image.jpg')]


class MainMenu:
    def __init__(self, title, surface_dimensions, theme=app_theme.get_theme()):
        # self.conf_profile_menu = None
        self.play_button = None
        self.image_widget = None
        self.selected_game = get_game_list_menu()[0][0]
        self.players = [pygame_menu.widgets.widget.textinput.TextInput, pygame_menu.widgets.widget.textinput.TextInput]
        self.username = [pygame_menu.widgets.widget.textinput.TextInput, pygame_menu.widgets.widget.textinput.TextInput]
        self.custom_theme = theme
        self.title = title
        self.surface_height, self.surface_width = surface_dimensions
        self.menu_height = surface_dimensions[0] * 0.75
        self.menu_width = surface_dimensions[1] * 0.75
        self.app_menu = None
        self.selected_game_index = 0
        self.sub_menu = None

        self.game_modes = {}
        for i in range(len(get_game_list_menu())):
            game = get_game_list_menu()[i][0]
            img_path = get_game_list_menu()[i][2]
            self.game_modes[i] = {
                'image': pygame_menu.BaseImage(image_path=os.path.join(PROJ_DIR_IMG, img_path)).scale(0.15, 0.15),
                'label': {'title': game}
            }

        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((self.surface_width, self.surface_height))

    def set_title(self, title):
        self.title = title

    # def set_window_dimensions(self, width, height):
    #     self.surface_height = height


    def start_selected_game(self):
        """
        register players and start the selected game
        :return:
        """
        # needs some work if we want it to be able to start additional games
        two_player = False
        player1 = self.players[0].get_value()
        player2 = self.players[1].get_value()

        reg.register_player(player1)
        print(f"Registered Player 1: {player1}")
        if player2 != "":
            print(f"Registered Player 2: {player2}")
            reg.register_player(player2)
            two_player = True

        flag = two_player
        print(flag)
        if not flag and self.selected_game_index == 0:
            print("Starting Dr. Mario in 1P...")
            dm.start_menu_1p(player1)
        elif not flag and self.selected_game_index == 1:
            print("Starting Puyo Puyo in 1P...")
            pm.start_menu_1p(player1)
        elif flag and self.selected_game_index == 0:
            print("Starting Dr. Mario in 2P...")
            dm.start_menu_2p(player1, player2)
        elif flag and self.selected_game_index == 1:
            print("Starting Puyo Puyo in 2P...")
            pm.start_menu_2p(player1, player2)
        else:
            print("No game selected!")

    def display_sub_menu(self):
        if self.sub_menu == 'register':
            self.reg_menu()
        elif self.sub_menu == 'profile':
            self.profile_menu()

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

        # initiate profile menu
        profile_menu = self.profile_menu()
        # initiate registration menu
        reg_menu = self.reg_menu()
        # initiate scoreboard menu
        # score_menu = self.score_menu()

        # Main Menu ----------------------------------------------------------
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
        # self.app_menu.add.horizontal_margin(self.menu_height/2)

        self.app_menu.add.button('Profile', profile_menu)
        # self.app_menu.add.vertical_margin(self.menu_width/2)

        # comment out if no SQL database
        #self.app_menu.add.button('Scoreboard', score_menu)
        # self.app_menu.add.horizontal_margin(self.menu_height/2)
        # self.play1 = reg_menu.add.button(f'Play {get_game_list_menu()[1][0]}', self.start_selected_game)
        self.app_menu.add.button('Quit', pygame_menu.events.EXIT)

    # comment out if no SQL database
    # def score_menu(self):
    #     # Scoreboard Menu
    #     score_menu = pygame_menu.Menu(
    #         height=self.menu_height,
    #         width=self.menu_width,
    #         theme=self.custom_theme,
    #         title='Scoreboard'
    #     )
    #     text = score.display_top_five()
    #     score_menu.add.button('Top Five Players').set_alignment(
    #         pygame_menu.locals.ALIGN_CENTER, )
    #     score_menu.add.button(text[0]).set_alignment(
    #         pygame_menu.locals.ALIGN_CENTER, )
    #     score_menu.add.button(text[1]).set_alignment(
    #         pygame_menu.locals.ALIGN_CENTER, )
    #     score_menu.add.button(text[2]).set_alignment(
    #         pygame_menu.locals.ALIGN_CENTER, )
    #     score_menu.add.button(text[3]).set_alignment(
    #         pygame_menu.locals.ALIGN_CENTER, )
    #     score_menu.add.button(text[4]).set_alignment(
    #         pygame_menu.locals.ALIGN_CENTER, )

    #     return score_menu

    def profile_menu(self):
        # Profile Menu
        profile_menu = pygame_menu.Menu(
            height=self.menu_height,
            width=self.menu_width,
            theme=self.custom_theme,
            title='Personal Profile'
        )

        def check_sql(profile_username):
            def get_input(input):
                player.change_username(profile_username, input)

            if player.check_if_player_exists(profile_username):
                input = profile_menu.add.text_input('New Name: ', maxchar=20, onreturn=get_input).set_alignment(
                    pygame_menu.locals.ALIGN_CENTER, )
                text = profile.display_score(profile_username)
                profile_menu.add.button(text[0]).set_alignment(
                    pygame_menu.locals.ALIGN_CENTER, )
                profile_menu.add.button(text[1]).set_alignment(
                    pygame_menu.locals.ALIGN_CENTER, )

        self.username = profile_menu.add.text_input('Username: ', maxchar=20, onreturn=check_sql).set_alignment(
            pygame_menu.locals.ALIGN_CENTER, )
        # profile_back_btn = profile_menu.add.button('Back', pygame_menu.events.BACK)
        # profile_quit_btn = profile_menu.add.button('Quit', pygame_menu.events.EXIT)
        #
        # profile_back_btn.translate(-210, 190)
        # profile_quit_btn.translate(210, 110)

        return profile_menu

    def reg_menu(self):
        # Registration menu
        reg_menu = pygame_menu.Menu(
            height=self.menu_height,
            width=self.menu_width,
            theme=self.custom_theme,
            title='Register Players'
        )

        self.players[0] = reg_menu.add.text_input('Player 1: ', maxchar=20, input_underline_hmargin=5) \
            .set_margin(400, 0).set_alignment(pygame_menu.locals.ALIGN_LEFT, )
        self.players[1] = reg_menu.add.text_input('Player 2: ', maxchar=20, default="") \
            .set_margin(400, 0).set_alignment(pygame_menu.locals.ALIGN_LEFT, )

        self.image_widget = reg_menu.add.image(
            image_path=self.game_modes[self.selected_game_index]['image'],
            padding=(25, 0, 0, 0),  # top, right, bottom, left
            scale=(0.15, 0.15),
            align=pygame_menu.locals.ALIGN_LEFT,
            set_margin=(400, 400)
        )

        # Profile Menu
        profile_menu = pygame_menu.Menu(
            height=self.menu_height,
            width=self.menu_width,
            theme=self.custom_theme,
            title='Personal Profile'
        )

        self.play_button = reg_menu.add.button(f'Play', self.start_selected_game)

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
        return reg_menu

    # def add_back_quit(self, menu):
    #
    #     back_btn = menu.add.button('Back', pygame_menu.events.BACK)
    #     quit_btn = menu.add.button('Quit', pygame_menu.events.EXIT)
    #
    #     return back_btn, quit_btn


if __name__ == '__main__':
    menu = MainMenu(app_theme.APP_TITLE, (app_theme.SURFACE_HEIGHT, app_theme.SURFACE_WIDTH), app_theme.get_theme())
    # menu.set_title(app_theme.APP_TITLE)
    menu.start_menu()
    menu.app_menu.mainloop(menu.surface, bgfun=draw_background)
