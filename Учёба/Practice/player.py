import pygame 

class Player():
    
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('тут картинка')
        self.rect = self.image.get_rect()

