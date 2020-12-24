import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, FLOOR_Y_POS))
    screen.blit(floor_surface, (floor_x_pos+SCREEN_WIDTH, FLOOR_Y_POS))

def create_pipe():
    random_pipe_pos = random.choice(pipe_heights)
    bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos-300))
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= SCREEN_HEIGHT:
            # must be the bottom pipe
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe_surface = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe_surface, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            print('collision')
    if bird_rect.top <= -100 or bird_rect.bottom >= FLOOR_Y_POS:
        print('top or bottom collision')

pygame.init()

SCREEN_WIDTH = 576
SCREEN_HEIGHT = 1024

FLOOR_Y_POS = 900

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Game Variables
gravity = 0.25
bird_movement = 0

FPS = 120

# Background
bg_surface = pygame.image.load('sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

# Floor
floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# Bird
bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x((bird_surface))
bird_rect = bird_surface.get_rect(center=(100, SCREEN_HEIGHT/2))

# Pipes
pipe_surface = pygame.image.load('sprites/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) # in milliseconds
pipe_heights = [400, 600, 800]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -12
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface, (0, 0))

    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    check_collision(pipe_list)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -SCREEN_WIDTH:
        floor_x_pos = 0
    
    pygame.display.update()
    clock.tick(FPS)
