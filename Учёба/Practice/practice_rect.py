import sys 
import pygame

from settings import *


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Практика')

flag = True


while flag:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        y += speed

    screen.fill(bg_color)
    pygame.draw.rect(screen, (199,100,100),(x, y,width, height))

  
    pygame.display.update()
    

    