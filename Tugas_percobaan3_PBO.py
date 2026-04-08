import pygame
pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Polisi vs Maling")

WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 40)

class Character:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.size = 40

    def draw(self, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))

    def batas_layar(self):
        if self.x < 0:
            self.x = 0
        if self.x > width - self.size:
            self.x = width - self.size
        if self.y < 0:
            self.y = 0
        if self.y > height - self.size:
            self.y = height - self.size


class Polisi(Character):
    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed


class Maling(Character):
    def move(self, keys):
        global maling_sembunyi, waktu_sembunyi

        if not maling_sembunyi:
            if keys[pygame.K_a]:
                self.x -= self.speed
            if keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_w]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed

            if (self.x < 0 or self.x > width or
                self.y < 0 or self.y > height):

                maling_sembunyi = True
                waktu_sembunyi = pygame.time.get_ticks()



polisi = Polisi(100, 100, 5)
maling = Maling(300, 200, 5)

clock = pygame.time.Clock()
running = True

game_over = False
win_time = 0

maling_sembunyi = False
waktu_sembunyi = 0


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # GERAK
    if not game_over:
        polisi.move(keys)
        maling.move(keys)
        polisi.batas_layar()


    if maling_sembunyi:
        if pygame.time.get_ticks() - waktu_sembunyi > 3000:
            maling_sembunyi = False
            maling.x = width // 2
            maling.y = height // 2

    if (not game_over and not maling_sembunyi and
        polisi.x < maling.x + maling.size and
        polisi.x + polisi.size > maling.x and
        polisi.y < maling.y + maling.size and
        polisi.y + polisi.size > maling.y):

        print("POLISI MENANG")
        game_over = True
        win_time = pygame.time.get_ticks()

    screen.fill(WHITE)

    polisi.draw((0, 0, 255))

    if not maling_sembunyi:
        maling.draw((255, 0, 0))

    if maling_sembunyi:
        text2 = font.render("MALING SEDANG BERSEMBUNYI", True, (255, 0, 0))
        screen.blit(text2, (50, 50))

    if game_over:
        text = font.render("===POLISI MENANG===", True, (0, 0, 0))
        screen.blit(text, (150, 180))

        # auto close setelah 3 detik
        if pygame.time.get_ticks() - win_time > 1000:
            running = False

    pygame.display.update()

pygame.quit()