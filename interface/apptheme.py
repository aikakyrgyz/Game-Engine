import pygame_menu

APP_TITLE = "<Placeholder Title>"
SURFACE_WIDTH = 1000
SURFACE_HEIGHT = 700
BACKGROUND_COLOR = (24, 24, 64, 90)    # DARK BLUE
ACCENT_COLOR = (255, 255, 255)
SELECT_FONT_COLOR = (170, 226, 255)     # LIGHT BLUE
TITLE_BACKGR_COLOR = (55, 65, 90, 190)  # GREY BLUE
HEADING_FONT_COLOR = (250, 231, 100)    # YELLOW
HEADING_FONT = pygame_menu.font.FONT_DIGITAL
FONT = pygame_menu.font.FONT_MUNRO


def get_theme():
    return pygame_menu.Theme(title_font=HEADING_FONT,
                             title_font_color=HEADING_FONT_COLOR,
                             title_font_shadow=True,
                             title_background_color=TITLE_BACKGR_COLOR,
                             widget_font=FONT,
                             widget_font_color=ACCENT_COLOR,
                            #  background_color=(0, 0, 0, 0),  # transparent background
                             background_color=BACKGROUND_COLOR,  # 75% opacity
                             # title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
                             widget_padding=25,
                             selection_color=SELECT_FONT_COLOR,
                             widget_selection_effect=pygame_menu.widgets.HighlightSelection(border_width=1,
                                                                                            margin_x=16,
                                                                                            margin_y=8)
                             )