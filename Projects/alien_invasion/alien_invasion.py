import sys
import pygame

from settings import Settings 

#Function котороая запускает игру и инициализирует параметры
def run_game():
    pygame.init()  
    #Cоздание объекта класса Settings из которо берём размеры экрана, и цвет бекграунда bg_color
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Инопланетное вторжение')
    ship = Ship(screen)

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color) 
        ship.blitme()       
        #Flip - отрисовывает последнего прорисованного экрана
        pygame.display.flip()
       

run_game()

