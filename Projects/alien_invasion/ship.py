import pygame

class Ship():
    def __init__(self, screen):
        '''Инициализирует корабль и создаёт его начальную позицию'''
        self.screen = screen
        #Загрузка спрайта главного героя и получение прямоугольника
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #Каждый новый корабль появляется внизу экрана(координаты)
    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)