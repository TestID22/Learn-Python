import sys
import pygame
import game_functions as gf

from ship import Ship
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
        gf.check_events(ship)
        gf.screen_update(ai_settings, screen, ship)

run_game()

