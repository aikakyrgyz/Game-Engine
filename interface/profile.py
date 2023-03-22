import pygame
import pygame_menu
import apptheme
from database import player, score


def profile_menu():

    pygame.display.set_caption(apptheme.APP_TITLE)
    reg_menu = pygame_menu.Menu(title="Player Registration",
                                width=apptheme.SURFACE_WIDTH * .75,
                                height=apptheme.SURFACE_HEIGHT * .75,
                                theme=apptheme.get_theme()
                                )

    reg_menu.add.button('Back', pygame_menu.events.EXIT)
    reg_menu.add.button('Quit', pygame_menu.events.EXIT)