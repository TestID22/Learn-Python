import sys
import pygame


def check_events(ship):
    '''обрабатывает цикл игры и нажатие клавиш'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.rect.centerx += 10
            elif event.key == pygame.K_a:
                ship.rect.centerx -= 10

def screen_update(ai_settings, screen, ship,):
    screen.fill(ai_settings.bg_color) 
    ship.blitme()       
    #Flip - отрисовывает последнего прорисованного экрана
    pygame.display.flip()