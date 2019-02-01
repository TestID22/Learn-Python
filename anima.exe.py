import pygame 
import sys
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Анимированный Квадрат')

while 1:
    pygame.time.delay(10)
    x = 10
    y = 10
    width = 100
    height = 100
    speed = 20
    pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        x = 200
        y = 10
        width = 100
        height = 100
        speed = 20
        pygame.draw.rect(screen,(255,0,0),(x,y,width,height))
            

    screen.fill((0,0,0))
    pygame.display.update()
    screen.fill((0,0,0))
    