import sys
import pygame
from pygame.locals import *
import random

tile_size = 4
tile_amount = tile_width, tile_height = 150, 100
random = True
screen = pygame.display.set_mode(size)
white = (255, 255, 255)

def make_grid (width, height, random):
    grid = []
    for i in range(width):
        row = []
        for j in range(height):
            tile_value = 0 if not random else randint(0,1)
            row.append(tile_value)
        grid.append(row)
    return grid


def update(dt, total_dt, fps_counter):
    total_dt = total_dt + dt
    if (total_dt >= 1000) :
        total_dt = total_dt - 1000
        pygame.display.set_caption('Game Of Life | FPS = ' + str(fps_counter))
        fps_counter = 0

    fps_counter = fps_counter + 1


def draw(screen, grid, tile_size, tile_width, tile_height):
    for i in grid
        for j in i
            pygame.draw.rect(screen, white, ())

def main():
    size = width, height = tile_width * tile_size, tile_height * tile_size

    pygame.init()

    fps = 60
    fpsClock = pygame.time.Clock()

    screen.fill((0, 0, 0))

    fps_counter = 0
    total_dt = 0

    current_grid = make_grid(width, height, random)
    next_grid = current_grid.copy()

    #init(current_grid, next_grid, width, height, random)
    dt = 1/fps
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        update(dt, total_dt, fps_counter)
        draw(screen, current_grid, tile_size, tile_width, tile_height)
        
        pygame.display.flip()
        dt = fpsClock.tick(fps)

main()