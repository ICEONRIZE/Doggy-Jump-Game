import pygame
import pygame_menu
from pygame_menu.font import FONT_MUNRO
import doggy_jump_main
import doggy_jump_menu


# Lost menu screen:
lost_menu_screen = pygame.display.set_mode((1100, 600))


# Restart function:
def restart_function():
    doggy_jump_main.points = 0
    doggy_jump_main.game_speed = 10
    doggy_jump_main.main()


# Quite function:
def quite_function():
    doggy_jump_main.points = 0
    doggy_jump_main.game_speed = 10
    doggy_jump_menu.game_menu()


# Dog draw function:
def draw_dog(screen):
    player = doggy_jump_main.front_img
    screen.blit(player, (1100 - 580, 500))


# Lose screen main function:
def lose_main():

    # Custom lost game menu theme:
    lost_menu_font = FONT_MUNRO
    lost_menu_title_bar = pygame_menu.widgets.MENUBAR_STYLE_NONE
    lost_background_image = pygame_menu.baseimage.path.join('../assets/grass_background.png')
    lost_menu_background = pygame_menu.baseimage.BaseImage(image_path=lost_background_image, drawing_offset=(0, 0))

    lose_menu_screen = pygame_menu.Theme(background_color=lost_menu_background, title_bar_style=lost_menu_title_bar)

    # Lose screen:
    lose_screen = pygame_menu.Menu("", 1100, 600, center_content=True,
                                   theme=lose_menu_screen)

    # Lose screen content:
    lose_text = lose_screen.add.label('YOU LOST!', selection_color=(80, 154, 255),font_name=lost_menu_font,
                                      font_color=(89, 145, 54))
    score_button = lose_screen.add.label('YOUR TOTAL SCORE IS: ' + str(doggy_jump_main.points), font_name=lost_menu_font,
                                         font_color=(89, 145, 54))
    restart_button = lose_screen.add.button("RESTART",  action=restart_function, selection_color=(80, 154, 255),
                                            font_name=lost_menu_font, font_color=(89, 145, 54))
    quit_button = lose_screen.add.button('QUIT', quite_function, selection_color=(80, 154, 255),
                                         font_name=lost_menu_font, font_color=(89, 145, 54))

    # Arrow parameters:
    arrow = arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

    # Lose main game loop:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if lose_screen.is_enabled:
            lose_screen.update(events)
            lose_screen.draw(lost_menu_screen)
            if lose_screen.get_current().get_selected_widget():
                arrow.draw(lost_menu_screen, lose_screen.get_current().get_selected_widget())

        draw_dog(lost_menu_screen)

        pygame.display.update()
