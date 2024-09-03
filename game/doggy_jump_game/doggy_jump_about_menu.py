import pygame
import pygame_menu
from pygame_menu.font import FONT_MUNRO
import doggy_jump_menu

# Screen variables:
pygame.init()

screen_width = 1100
screen_height = 600
menu_screen = pygame.display.set_mode((screen_width, screen_height))

# Game menu variables:
# Custom game menu theme:
menu_font = FONT_MUNRO
background_image = pygame_menu.baseimage.path.join('../assets/grass_background.png')

menu_background = pygame_menu.baseimage.BaseImage(image_path=background_image, drawing_offset=(0, 0))

menu_theme = pygame_menu.Theme(title_background_color=(89, 145, 54), title_font=menu_font, title_font_size=50,
                               title_font_color=(80, 154, 255), widget_font=menu_font,
                               background_color=menu_background, title_font_shadow=True)


# Comeback to the main menu function:
def back_to_menu():
    doggy_jump_menu.game_menu()


# About menu screen:
about_menu_panel = pygame_menu.Menu('Here you can read game description', 1100, 600, theme=menu_theme)

# About menu content:
about_menu_panel.add.label("Even DOGGY Jump is small platformer mini-game, it has IT'S OWN PLOT: ",
                           font_color=(80, 154, 255))
about_menu_panel.add.vertical_margin(50)
about_menu_panel.add.label("Masha and her 'favourite friend' Racks went for trip, \n"
                           "but on they way Racks lost and now he have to find Masha ", font_color=(80, 154, 255))
# Button comeback:
button_quit = about_menu_panel.add.button('BACK', action=back_to_menu, selection_color=(80, 154, 255),
                                          font_color=(89, 145, 54))
# Arrow for the selected menu option:
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))


def about_game():
    # Menu mainloop:
    about_menu = True
    while about_menu:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if about_menu_panel.is_enabled:
            about_menu_panel.update(events)
            about_menu_panel.draw(menu_screen)

        pygame.display.update()
