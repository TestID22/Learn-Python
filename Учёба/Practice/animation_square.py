import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))

my_image = pygame.image.load('хачан.jpeg')

while True:
    for e in pygame.event.get():
        e.type == pygame.QUIT:
            sys.exit()