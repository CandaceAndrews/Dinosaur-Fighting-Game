import pygame
from Fighter import Fighter

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Fighter")

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define colors
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (21, 163, 108)
WHITE = (255, 255, 255)

# define fighter variables
DIABLO_SIZE = 1330
DIABLO_SCALE = 4
DIABLO_OFFSET = [78, 43]
DIABLO_DATA = [DIABLO_SIZE, DIABLO_SCALE, DIABLO_OFFSET]
SAURON_SIZE = 1330
SAURON_SCALE = 3
SAURON_OFFSET = [83, 56]
SAURON_DATA = [SAURON_SIZE, SAURON_SCALE, SAURON_OFFSET]

# load background image
bg_image = pygame.image.load("assets/images/background/bg.png").convert_alpha()

# load spritesheets
diablo_sheet = pygame.image.load(
    "assets/images/diablo/sprites/diablo.png").convert_alpha()
sauron_sheet = pygame.image.load(
    "assets/images/sauron/sprites/sauron.png").convert_alpha()

# define number of steps in each animation
DIABLO_ANIMATION_STEPS = [5, 5, 4, 2]
SAURON_ANIMATION_STEPS = [5, 5, 4, 2]


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))


# create two instances of fighters
fighter_1 = Fighter(200, 310, False, DIABLO_DATA, diablo_sheet,
                    DIABLO_ANIMATION_STEPS)
fighter_2 = Fighter(700, 310, True, SAURON_DATA, sauron_sheet,
                    SAURON_ANIMATION_STEPS)


# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_bg()

    # show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    # move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)

    # update fighters
    fighter_1.update()
    fighter_2.update()

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update background
    pygame.display.update()

# exit game
pygame.quit()
