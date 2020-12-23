import pygame, sys

pygame.init()

SCREEN_WIDTH = 576
SCREEN_HEIGHT = 1024

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

FPS = 120

bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    pygame.display.update()
    clock.tick(FPS)
