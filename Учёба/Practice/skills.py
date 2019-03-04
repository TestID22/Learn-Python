import pygame
import sys

#Установка разрешения экрана игры
win = pygame.display.set_mode((500, 600))
#Тут подпись вкладки 
pygame.display.set_caption("Pygame")

#переменные игррка и игры в целом
x = 450
y = 500
width = 30
height = 30
speed = 10
#функция отрисовки 
def render():
    win.fill((0,0,0))      
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.flip()

#освной цикл игры + управление персонажем 
while True:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and y > 10:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed

    
render()



pygame.quit()