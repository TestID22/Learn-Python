import sys

import pygame



pygame.init()
win = pygame.display.set_mode((300,300))
pygame.display.set_caption("Чмунька:Месть Вени")

x = 50
y = 50
width = 40
height = 60
speed = 5

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				sys.exit(0)

	pygame.draw.rect(win, (107,170,188),(x,y, width, height))
	pygame.display.update()
	pygame.display.flip()


pygame.quit()
 