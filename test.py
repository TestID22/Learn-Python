import pygame
 
FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 100
 
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
pygame.init()
 
clock = pygame.time.Clock()
 
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
 
# радиус и координаты круга
r = 30
x = 0 - r  # скрываем за левой границей
y = WIN_HEIGHT // 2  # выравнивание по центру по вертикали
 
while 1:
    sc.fill(WHITE)
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
 
    pygame.draw.circle(sc, ORANGE, (x, y), r)
 
    pygame.display.update()
 
    # если полностью скрылся за правой границей
    if x >= WIN_WIDTH + r:
        x = 0 - r
    else:  # во всех остальных случаях
        x += 2  # в следующем кадре круг сместится,
        # от значения зависит "скорость движения"
 
    clock.tick(FPS)