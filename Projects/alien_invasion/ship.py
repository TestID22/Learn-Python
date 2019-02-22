import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        '''Инициализирует корабль и создаёт его начальную позицию'''
        self.screen = screen

        self.ai_settings = ai_settings

        self.screen_rect = screen.get_rect()
        #Загрузка спрайта главного героя и получение прямоугольника
        self.image = pygame.image.load('images\хачан.jpg')
        self.rect = self.image.get_rect()
        
        #Каждый новый корабль появляется внизу экрана(координаты)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #флаг для непрерывного передвижения 
        self.moving_right = False
        self.moving_left = False

        #Сохранение вещественной координаты корабля
        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

        self.rect.centerx = self.center

    def blitme(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image, self.rect)