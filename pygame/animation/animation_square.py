import sys
import pygame
import time

pygame.init()

WIDTHSCREEN = 300
HEIGHTSCREEN = 300

screen = pygame.display.set_mode((WIDTHSCREEN,HEIGHTSCREEN))
pygame.display.set_caption('Анимация')

DOWNLEFT = 'downleft'
DOWNRIGT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

SPEED = 2

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

x = 0
y = 150

box_1 = {'rect':pygame.Rect(0, 100, 40,40),'color':green, 'dir':DOWNRIGT}

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if box_1['dir'] == DOWNRIGT:
            box_1['rect'].left += SPEED
            box_1['rect'].top += SPEED
        if box_1['dir'] == DOWNLEFT:
            box_1['rect'].left -= SPEED
            box_1['rect'].top += SPEED
        if box_1['dir'] == UPRIGHT:
            box_1['rect'].left += SPEED
            box_1['rect'].top -= SPEED
        if box_1['dir'] == UPLEFT:
            box_1['rect'].left -= SPEED
            box_1['rect'].top -= SPEED
        
        if box_1['rect'].bottom > 300:
            if box_1['dir'] == DOWNLEFT:
                box_1['dir'] = UPLEFT
            if box_1['dir'] == DOWNRIGT:
                box_1['dir'] = UPRIGHT 
        if box_1['rect'].top < 0:
            if box_1['dir'] == UPLEFT:
                box_1['dir'] = DOWNLEFT
            if box_1['dir'] == UPRIGHT:
                box_1['dir'] = DOWNRIGT
        if box_1['rect'].left < 0:
            if box_1['dir'] == DOWNLEFT:
                box_1['dir'] = DOWNRIGT
            if box_1['dir'] == UPLEFT:
                box_1['dir'] = UPRIGHT
        if box_1['rect'].right > 300:
            if box_1['dir'] == DOWNRIGT:
                box_1['dir'] = DOWNLEFT
            if box_1['dir'] == UPRIGHT:
                box_1['dir'] = UPLEFT    

        screen.fill(white)  
        pygame.draw.rect(screen, box_1['color'],box_1['rect'])
        pygame.display.update()

