import sys
import pygame


pygame.init()
screen = pygame.display.set_mode((800,500))

class Main():
    def __init__(self,screen):
        self.screen = screen
        self.back = pygame.image.load('D:\Code\Python\Учёба\Practice\\back.jpg')
        self.main_loop()
        
    def render(self):
        '''Отвечает за отрисовку элементов на экране'''
        self.screen.blit(self.back, (0, -300))
        pygame.display.flip()

    def main_loop(self):
        while True:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
            self.render()
            
main = Main(screen) 
