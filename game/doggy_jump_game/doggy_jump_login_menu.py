import pygame
import pygame_menu
from pygame_menu.font import FONT_MUNRO
import doggy_jump_menu


# Screen variables:
pygame.init()

screen_width = 1100
screen_height = 600
menu_screen = pygame.display.set_mode((screen_width, screen_height))
inputted_name = 'USER'

# Game menu variables:
# Custom game menu theme:
menu_font = FONT_MUNRO
background_image = pygame_menu.baseimage.path.join('../assets/grass_background.png')

menu_background = pygame_menu.baseimage.BaseImage(image_path=background_image, drawing_offset=(0, 0))

menu_theme = pygame_menu.Theme(title_background_color=(89, 145, 54), title_font=menu_font, title_font_size=50,
                               title_font_color=(80, 154, 255), widget_font=menu_font,
                               background_color=menu_background, title_font_shadow=True)


# Menu function to save inputted name:
def get_inputted_name(value):
    global inputted_name
    inputted_name = value


# Return to main menu from Login Menu
def back_to_start_menu(value):
    value = inputted_name
    update_title = doggy_jump_menu.start_menu_panel.set_title('Welcome to DOGGY JUMP, ' + inputted_name)
    doggy_jump_menu.game_menu()


# Login menu main screen:
login_menu_panel = pygame_menu.Menu('You can choose your name here', 1100, 600, theme=menu_theme)

# Login menu content:
login_menu_panel.add.text_input('NICKNAME: ', default='USER', maxchar=11, font_size=30,
                                onchange=get_inputted_name, onreturn=back_to_start_menu,
                                selection_color=(89, 145, 54))

# Arrow for the selected menu option:
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))


def login_game():
    # Menu mainloop:
    login_menu = True
    while login_menu:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if login_menu_panel.is_enabled:
            login_menu_panel.update(events)
            login_menu_panel.draw(menu_screen)

        pygame.display.update()
