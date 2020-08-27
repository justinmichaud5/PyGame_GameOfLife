import pygame
from pygame.locals import *
import random

size = width, height = 320, 240


pygame.init()
screen = pygame.display.set_mode(size)

while True :
    color = random.randrange(255), random.randrange(255), random.randrange(255)
    screen.fill(color)
