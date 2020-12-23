import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos+SCREEN_WIDTH, 900))

pygame.init()

SCREEN_WIDTH = 576
SCREEN_HEIGHT = 1024

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

FPS = 120

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))

    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -SCREEN_WIDTH:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(FPS)
