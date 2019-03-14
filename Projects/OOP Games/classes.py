import pygame

class Player():
    def __init__(self,):
        self.image = pygame.image.load('D:\Code\Python\Projects\OOP Games\\my_asleep_reflection.png')
        self.name = 'MyAsleepReflection'
        self.pos_x = 50
        self.pos_y = 340
        self.moving_right = False
      
    def render(self, screen):
        screen.blit(self.image,(self.pos_x,self.pos_y,100,150))
    
