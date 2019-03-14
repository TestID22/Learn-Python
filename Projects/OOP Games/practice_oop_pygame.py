import sys
import pygame
from classes import Player

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('My Asleep Reflections')

class Main():
    def __init__(self,screen):
        self.screen = screen
        self.back = pygame.image.load('D:\Code\Python\Projects\OOP Games\\1.jpg')
        self.player = Player()
        self.main_loop()
        
    def render(self):
        '''Отвечает за отрисовку элементов на экране'''
        self.screen.blit(self.back, (0, -300))
        self.player.render(screen)

        pygame.display.flip()
        pygame.mouse.set_visible(False)

    def main_loop(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_RIGHT:
                        self.player.pos_x += 10
                    if i.key == pygame.K_LEFT:
                        self.player.pos_x -= 10

            self.render()

            
main = Main(screen) 
