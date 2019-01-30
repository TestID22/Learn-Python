import pygame
import sys


win = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Happy Pink Square")

x = 450
y = 500
width = 30
height = 30
speed = 10


while True:
    pygame.time.delay(30)
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

    
    win.fill((0,0,0))      
    pygame.draw.rect(win, (255,20,100), (x, y, width, height))
    pygame.display.update()
   



