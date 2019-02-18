import pygame
import sys


win = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Happy Pink Square")
#my_image = pygame.image.load('======')
x = 200
y = 200
width = 30
height = 30
speed = 10


while True:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 10:
        y -= speed
    if keys[pygame.K_s] and y < 560:
        y += speed
    if keys[pygame.K_a] and x > 10:
        x -= speed
    if keys[pygame.K_d] and x < 460:
        x += speed
    if event.type == pygame.MOUSEBUTTONDOWN:
        x,y = event.pos

    
    win.fill((0,0,0))      
    pygame.draw.rect(win, (255,20,100), (x, y, width, height))
    pygame.display.update()
    
            
            
            

      
    
        
  
        
       
            
     



