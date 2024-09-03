import pygame
import pygame_menu
from pygame_menu.font import FONT_MUNRO
import doggy_jump_main
import doggy_jump_menu

# Win screen
win_menu_screen = pygame.display.set_mode((1100, 600))
owner_img = pygame.image.load('../assets/Owner.png')


# Draw dog function:
def draw_dog(screen):
    player = doggy_jump_main.run_img[0]
    screen.blit(player, (1100 - 620, 500))


# Draw dog function:
def draw_owner(screen):
    player = owner_img
    screen.blit(player, (1100 - 510, 470))


def restart_function():
    doggy_jump_menu.game_menu()


# Main win screen function:
def win_main():
    win_menu_font = FONT_MUNRO
    win_menu_title_bar = pygame_menu.widgets.MENUBAR_STYLE_NONE
    win_background_image = pygame_menu.baseimage.path.join('../assets/grass_background.png')
    win_menu_background = pygame_menu.baseimage.BaseImage(image_path=win_background_image, drawing_offset=(0, 0))

    winning_menu_screen = pygame_menu.Theme(background_color=win_menu_background, title_bar_style=win_menu_title_bar)

    # Win screen:
    win_screen = pygame_menu.Menu("", 1100, 600, center_content=True,
                                  theme=winning_menu_screen)

    # Win screen content:
    win_text = win_screen.add.label('YOU WIN!', selection_color=(80, 154, 255), font_name=win_menu_font,
                                    font_color=(89, 145, 54))
    restart_button = win_screen.add.button("RESTART", action=restart_function, selection_color=(80, 154, 255),
                                           font_name=win_menu_font, font_color=(89, 145, 54))
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if win_screen.is_enabled:
            win_screen.update(events)
            win_screen.draw(win_menu_screen)

        draw_dog(win_menu_screen)
        draw_owner(win_menu_screen)

        pygame.display.update()
