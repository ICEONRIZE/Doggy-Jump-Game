import pygame
import pygame_menu
from pygame_menu.font import FONT_MUNRO
import doggy_jump_main
import doggy_jump_about_menu
import doggy_jump_login_menu

# Screen variables:
pygame.init()
screen_width = 1100
screen_height = 600
menu_screen = pygame.display.set_mode((screen_width, screen_height))


# Start menu function:
def game_start_function():
    doggy_jump_main.main()


# Function for difficulty selection:
def set_difficulty_function(value, dif):
    if value[0][1] == 0:
        doggy_jump_main.game_speed = 10
        print('Easy')
    elif value[0][1] == 1:
        doggy_jump_main.game_speed = 15
        print('Medium')
    elif value[0][1] == 2:
        doggy_jump_main.game_speed = 20
        print('Hard')


# Function for game description:
def menu_about():
    doggy_jump_about_menu.about_game()


# Menu log in function:
def menu_login():
    doggy_jump_login_menu.login_game()


# Game menu variables:
# Custom game menu theme:
menu_font = FONT_MUNRO
background_image = pygame_menu.baseimage.path.join('../assets/grass_background.png')

menu_background = pygame_menu.baseimage.BaseImage(image_path=background_image, drawing_offset=(0, 0))

menu_theme = pygame_menu.Theme(title_background_color=(89, 145, 54), title_font=menu_font, title_font_size=50,
                               title_font_color=(80, 154, 255), widget_font=menu_font,
                               background_color=menu_background, title_font_shadow=True)

# Menu title string
start_menu_panel = pygame_menu.Menu('Welcome to DOGGY JUMP, ' + doggy_jump_login_menu.inputted_name, 1100, 600,
                                    theme=menu_theme)

# Main content of game menu include buttons functions adn parameters:
button_login = start_menu_panel.add.button('LOG IN', menu_login, selection_color=(80, 154, 255),
                                           font_color=(89, 145, 54))
button_play = start_menu_panel.add.button('PLAY', game_start_function, selection_color=(80, 154, 255),
                                          font_color=(89, 145, 54))
button_difficulty = start_menu_panel.add.selector('DIFFICULTY: ', [('Easy', 0), ('Medium', 1), ('Hard', 2)],
                                                  onchange=set_difficulty_function, selection_color=(80, 154, 255),
                                                  font_color=(89, 145, 54))
button_about = start_menu_panel.add.button('ABOUT', menu_about, selection_color=(80, 154, 255),
                                           font_color=(89, 145, 54))
button_quit = start_menu_panel.add.button('QUIT', pygame_menu.events.EXIT, selection_color=(80, 154, 255),
                                          font_color=(89, 145, 54))

# Arrow for the selected menu option:
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))


# Game Menu:
def game_menu():
    # Menu mainloop:
    start_menu = True
    while start_menu:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if start_menu_panel.is_enabled:
            start_menu_panel.update(events)
            start_menu_panel.draw(menu_screen)
            if start_menu_panel.get_current().get_selected_widget():
                arrow.draw(menu_screen, start_menu_panel.get_current().get_selected_widget())

        pygame.display.update()
