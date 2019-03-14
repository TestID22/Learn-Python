import pygame

class Player():
    def __init__(self,):
        self.image = pygame.image.load('D:\Code\Python\Projects\OOP Games\\my_asleep_reflection.png')
        self.name = 'Вова Кудрявый'
      
    def render(self, screen):
        screen.blit(self.image,(50,340,100,50))