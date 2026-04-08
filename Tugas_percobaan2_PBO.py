import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game PBO")

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 1
        self.color = BLUE

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def batas(self):
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width
        if self.y < 0:
            self.y = 0
        if self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height

    def pilih_warna(self, keys):
        if keys[pygame.K_1]:
            self.color = RED

    def pilih_warna2(self, keys):
        if keys[pygame.K_2]:
            self.color = BLUE

    def increase_size(self, keys):
        if keys[pygame.K_p]:
            self.width += 1
            self.height += 1

    def decrease_size(self, keys):
        if keys[pygame.K_o]:
            self.width -= 1
            self.height -= 1


    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.width, self.height))


player = Player(375,275)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.batas()
    player.pilih_warna(keys)
    player.pilih_warna2(keys)
    player.increase_size(keys)
    player.decrease_size(keys)
    screen.fill(WHITE)
    player.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()