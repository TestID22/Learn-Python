import pygame
import sys
from settings import *


pygame.init()


screen = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
pygame.display.set_caption("Игра Про Доставщика - Пашку")

x = 10
y = 340
height = 50
width = 50

while 1:
    pygame.time.delay(13)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.draw.rect(screen, (255,0,0),(x,y,height,width))        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and x < 480 - width:
        x += 10
    if keys[pygame.K_a] and x > 20:
        x -= 10
    pygame.display.update()
    screen.fill((0,0,0))
    