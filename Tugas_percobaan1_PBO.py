import pygame
import sys

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Praktikum PBO - Pygame")

MERAH = (255,0,0)
HIJAU = (0,255,0)
BIRU = (0,0,255)

screen.fill(BIRU)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.flip()

pygame.quit()
sys.exit()