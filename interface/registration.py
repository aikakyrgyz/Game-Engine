import pygame
import pygame_menu
import apptheme
from database import player


def register_player(username):
    if username != "" and len(username) <= 15:
        # comment out the function below if you do not have SQL set-up
        player.insert_username_into_player_table(username)
        # if exists in the database, add game to player profile
        print(f"Player profile updated - {username}")

        # else register player, add to database
        print(f"Player registered - {username}")
    else:
        print(f"Error, username too long!")


# def registration_menu():
#     """
#     registers a new user to the system
#     :return:
#     """
#     pygame.display.set_caption(apptheme.APP_TITLE)
#     reg_menu = pygame_menu.Menu(title="Player Registration",
#                                 width=apptheme.SURFACE_WIDTH * .75,
#                                 height=apptheme.SURFACE_HEIGHT * .75,
#                                 theme=apptheme.get_theme()
#                                 )
#
#     # dunno about this:
#     selected_game = reg_menu.get_index()
#     player1 = reg_menu.add.text_input('Player 1', default="_unspecified")
#     register_player(player1)
#
#     player2 = reg_menu.add.text_input('Player 2', default="")
#     if player2 != "":
#         register_player(player2)
#
#     reg_menu.add.button('Back', pygame_menu.events.EXIT)
#     reg_menu.add.button('Quit', pygame_menu.events.EXIT)
