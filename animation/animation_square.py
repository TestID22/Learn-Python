import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
window = pygame.surface((400,400))
my_image = pygame.image.load('player.png')
x = 10
y = 10
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    
    screen.fill((230,230,230))
    window.blit(my_image(x,y))
    pygame.display.update()
    