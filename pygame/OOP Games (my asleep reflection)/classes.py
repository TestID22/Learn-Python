import pygame

class Player():
    def __init__(self,):
        self.image = pygame.image.load(r'D:\Code\Python\pygame\OOP Games (my asleep reflection)\my_asleep_reflection.png')
        self.name = 'MyAsleepReflection'
        self.pos_x = 50
        self.pos_y = 340
        self.moving_right = False
      
    def render(self, screen):
        screen.blit(self.image,(self.pos_x,self.pos_y,100,150))
    
