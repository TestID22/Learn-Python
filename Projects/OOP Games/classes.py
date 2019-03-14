import pygame

class Player():
    def __init__(self, screen):
        self.image = pygame.image.load('D:\Code\Python\Projects\OOP Games\\player.png')
        self.name = 'Вова Кудрявый'
      
    def render(self, screen):
        self.screen.blit(self.image(50,50),(300,40,50,50))