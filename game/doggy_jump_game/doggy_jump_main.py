import pygame
import random
import doggy_jump_lose_menu
import doggy_jump_menu
import doggy_jump_win_menu

# Screen init:
pygame.init()

screen_height = 600
screen_width = 1100
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('DOGGY JUMP')
speed = 10
game_speed = 10
points = 0

# Image init:
run_img = [pygame.image.load('../assets/dog_first_step.png'),
           pygame.image.load('../assets/dog_last_step.png')]
stand_img = pygame.image.load('../assets/dog_stand.png')
front_img = pygame.image.load('../assets/dog_front.png')
sleep_img = pygame.image.load('../assets/dog_sleep.png')
jump_img = pygame.image.load('../assets/dog_jump.png')
chicken_img = pygame.image.load('../assets/chicken.png'),
ham_img = pygame.image.load('../assets/ham.png'),
sushi_img = pygame.image.load('../assets/sushi.png'),
grass = [pygame.image.load('../assets/grass_background.png').convert_alpha(),
         pygame.image.load('../assets/grass_background2.png').convert_alpha()]
stone_small = [pygame.image.load('../assets/stone_small.png'),
               pygame.image.load('../assets/stone_small1.png'),
               pygame.image.load('..//assets/stone_small2.png')]
stone_big = [pygame.image.load('../assets/stone_big.png'),
             pygame.image.load('../assets/stone_big1.png'),
             pygame.image.load('../assets/stone_big2.png')]


# Dog class:
class Dog:
    def __init__(self):
        self.dog_run = run_img
        self.dog_jump = jump_img
        self.dog_stand = stand_img
        self.dog_front = front_img
        self.dog_sleep = sleep_img

        self.dog_running = True
        self.dog_jumping = False
        self.dog_standing = False

        self.step_index = 0
        self.jump_vel = self.jump_velocity
        self.image = self.dog_run[0]

        # Dog rectangle collision and coordinates:
        self.dog_rect = self.image.get_rect()
        self.dog_rect_x = self.x_pos
        self.dog_rect_y = self.y_pos

    # Dog position:
    x_pos = 30
    y_pos = 500
    jump_velocity = 8.5

    # Movement update function:
    def update(self, user_input):
        # Update functions:
        if self.dog_running:
            self.running()
        if self.dog_jumping:
            self.jumping()

        # Statements for animation controlling:
        if self.step_index >= 10:
            self.step_index = 0

        # If statements for controlling dog movements:
        if user_input[pygame.K_SPACE] or user_input[pygame.K_w] or user_input[pygame.K_UP] and not self.dog_jumping:
            self.dog_running = False
            self.dog_jumping = True
            self.dog_standing = False
        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s] and not self.dog_jumping:
            self.dog_standing = True
            self.dog_jumping = False
            self.dog_running = False
        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d] and not self.dog_jumping:
            self.dog_jumping = False
            self.dog_running = True
            self.dog_standing = False

    # Dog running function
    def running(self):
        # Dog running velocity:
        global game_speed

        self.image = self.dog_run[self.step_index // 5]
        self.dog_rect_x = self.x_pos
        self.dog_rect_y = self.y_pos
        self.step_index += 1

    # Dog jumping function:
    def jumping(self):
        # Dog jumping velocity:
        global game_speed

        self.image = self.dog_jump

        # Dog jumping statements:
        if self.dog_jumping:
            self.dog_rect_y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.jump_velocity:
            self.dog_jumping = False
            self.dog_running = True
            self.jump_vel = self.jump_velocity
            self.dog_rect_x = self.x_pos
            self.dog_rect_y = self.y_pos

    def draw(self, screen):
        screen.blit(self.image, (self.dog_rect_x, self.dog_rect_y))


# Obstacles:
class Stones:

    # Obstacles variables:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.stones_rect = self.image[self.type].get_rect()
        self.stones_rect.x = screen_width

    # Obstacles update function:
    def update(self):
        self.stones_rect.x -= game_speed
        if self.stones_rect.x < -self.stones_rect.width:
            obstacles.pop()

    # Obstacles draw function:
    def draw(self, screen):
        screen.blit(self.image[self.type], self.stones_rect)


# Small Stones Obstacles:
class SmallStones(Stones):

    # SmallStones obstacle velocity:
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.stones_rect.y = 500


# Big Stones Obstacles:
class BigStones(Stones):

    # BigStones obstacles velocity:
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.stones_rect.y = 450


# Food Bonus Class:
class Food:
    # Food init function:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.food_rect = self.image[self.type].get_rect()
        self.food_rect.x = screen_width // 6
        self.food_rect.y = 500

    # Food update function:
    def update(self):
        self.food_rect.x -= game_speed
        if self.food_rect.x < -self.food_rect.width:
            bonus_food.pop()

    # Food draw function:
    def draw(self, screen):
        screen.blit(pygame.transform.scale(self.image[self.type], (50, 50)), self.food_rect)


class FoodManager(Food):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)


# Main function:
def main():
    # Global constant:
    global x_pos_bg, y_pos_bg, points, obstacles, bonus_food
    x_pos_bg = 0
    y_pos_bg = 0
    x_pos_bg2 = 0
    bonus_food = []
    obstacles = []
    eat = False

    # Constant values:
    run = True
    clock = pygame.time.Clock()
    player = Dog()

    font_name = pygame.font.match_font('TimesNewRoman')

    # Score function:
    def score(bool):
        global points, game_speed

        # Point updating condition:
        if bool:
            points += 10
            if points % 100 == 0:
                game_speed += 1
            if points == 4500:
                doggy_jump_win_menu.win_main()

        # Point draw inti:
        font = pygame.font.SysFont(font_name, 30)
        score_text = font.render('Points: ' + str(points), True, 'Red')
        text_rect = score_text.get_rect(center=(1000, 20))
        game_screen.blit(score_text, text_rect)

    # Main game loop:
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Background init:
        global game_speed

        game_screen.blit(grass[0], (x_pos_bg, y_pos_bg))
        game_screen.blit(grass[0], (grass[0].get_width() + x_pos_bg, y_pos_bg))

        # Background condition for screen changing:
        if x_pos_bg <= -grass[0].get_width():
            game_screen.blit(grass[1], (x_pos_bg2, y_pos_bg))
            game_screen.blit(grass[1], (grass[1].get_width() + x_pos_bg2, y_pos_bg))
            if x_pos_bg2 <= -grass[1].get_width():
                x_pos_bg = 0
                x_pos_bg2 = 0
                game_screen.blit(grass[0], (grass[0].get_width() + x_pos_bg, y_pos_bg))
            else:
                x_pos_bg2 -= game_speed
        else:
            x_pos_bg -= game_speed

        # User init:
        user_input = pygame.key.get_pressed()
        player.update(user_input)
        player.draw(game_screen)

        # Food collision check:
        if len(bonus_food) == 0:
            if random.randint(0, 2) == 0:
                bonus_food.append(FoodManager(chicken_img))
            elif random.randint(0, 2) == 1:
                bonus_food.append(FoodManager(ham_img))
            elif random.randint(0, 2) == 2:
                bonus_food.append(FoodManager(sushi_img))

        # Food init:
        for food in bonus_food:
            food.draw(game_screen)
            food.update()

            # Food hit collision and score system:
            if food.food_rect.collidepoint(player.dog_rect_x, player.dog_rect_y):
                bonus_food.pop()
                eat = True
                score(True)
            score(False)

        # Add stones obstacles conditions:
        if len(obstacles) == 0:
            if random.randint(0, 1) == 0:
                obstacles.append(SmallStones(stone_small))
            elif random.randint(0, 1) == 1:
                obstacles.append(BigStones(stone_big))

        # Obstacles init:
        for obstacle in obstacles:
            obstacle.draw(game_screen)
            obstacle.update()

            # Hit collision check
            if obstacle.stones_rect.collidepoint(player.dog_rect_x, player.dog_rect_y):
                doggy_jump_lose_menu.lose_main()

        clock.tick(30)
        pygame.display.update()
    pygame.quit()


# Checking function:
if __name__ == '__main__':
    doggy_jump_menu.game_menu()
