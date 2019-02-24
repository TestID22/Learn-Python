import pygame
import sys
import time

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Простая Анимация Объекта')
x = 100
y = 100
LEFT = 'left'
RIGHT = 'right'
SPEED = 4

box = {'rect':pygame.Rect(x,y, 50,50), 'color':(125,125,125), 'dir': LEFT}
#игровой цикл(основной цикл)
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

        if box['dir'] == LEFT:
            box['rect'].left += SPEED
        if box['dir'] == RIGHT:
            box['rect'].left -= SPEED

        if box['rect'].left > 400 - 50:
            if box['dir'] == LEFT:
                box['dir'] = RIGHT    

        if box['rect'].left < 0:
            if box['dir'] == RIGHT:
                box['dir'] = LEFT   

        screen.fill((255,255,255))
        pygame.draw.rect(screen,box['color'],box['rect'])
        pygame.display.update()