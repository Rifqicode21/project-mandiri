import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Farm Escape")

clock = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

class GameObject:

    def __init__(self,x,y,w,h,color):

        self.rect = pygame.Rect(x,y,w,h)
        self.color = color

    def draw(self):

        pygame.draw.rect(screen,self.color,self.rect)

class Player(GameObject):

    def __init__(self):

        super().__init__(280,550,40,40,GREEN)

        self.speed = 40

    def move(self,key):

        if key == pygame.K_LEFT:
            self.rect.x -= self.speed

        if key == pygame.K_RIGHT:
            self.rect.x += self.speed

        if key == pygame.K_UP:
            self.rect.y -= self.speed

        if key == pygame.K_DOWN:
            self.rect.y += self.speed

class Enemy(GameObject):

    def __init__(self,x,y,speed,direction):

        super().__init__(x,y,40,40,RED)

        self.speed = speed
        self.direction = direction


    def update(self):

        self.rect.x += self.speed * self.direction

        if self.direction == 1 and self.rect.x > WIDTH:
            self.rect.x = -40

        if self.direction == -1 and self.rect.x < -40:
            self.rect.x = WIDTH

class Item(GameObject):

    def __init__(self):

        x = random.randint(0,560)
        y = random.randint(100,500)

        super().__init__(x,y,20,20,YELLOW)


class Game:

    def __init__(self):

        self.player = Player()

        self.level = 1
        self.score = 0

        self.item = Item()

        self.enemies = []

        self.game_over = False
        self.win = False

        self.create_level()


    def create_level(self):

        self.enemies.clear()

        if self.level == 1:
            speed = 3

        elif self.level == 2:
            speed = 5

        else:
            speed = 7


        # 2 musuh ke kanan
        self.enemies.append(Enemy(0,200,speed,1))
        self.enemies.append(Enemy(100,350,speed,1))

        # 1 musuh ke kiri
        self.enemies.append(Enemy(500,120,speed,-1))


    def update(self):

        if self.game_over or self.win:
            return


        for enemy in self.enemies:

            enemy.update()

            if self.player.rect.colliderect(enemy.rect):

                self.game_over = True


        if self.player.rect.colliderect(self.item.rect):

            self.score += 1

            self.item = Item()

        if self.score >= 20:
            self.level = 3

        elif self.score >= 10:
            self.level = 2

        else:
            self.level = 1

        if self.score == 10 or self.score == 20:
            self.create_level()

        if self.score >= 23:
            self.win = True


    def draw(self):

        screen.fill((0,0,0))

        self.player.draw()

        self.item.draw()

        for enemy in self.enemies:
            enemy.draw()

        font = pygame.font.SysFont(None,36)

        score_text = font.render(f"Score : {self.score}",True,WHITE)
        level_text = font.render(f"Level : {self.level}",True,WHITE)

        screen.blit(score_text,(10,10))
        screen.blit(level_text,(10,40))

        pygame.display.update()


    def draw_game_over(self):

        screen.fill((0,0,0))

        font_big = pygame.font.SysFont(None,72)
        font_small = pygame.font.SysFont(None,36)

        text1 = font_big.render("GAME OVER",True,RED)
        text2 = font_small.render(f"Score : {self.score}",True,WHITE)
        text3 = font_small.render("Press R to Restart",True,WHITE)

        screen.blit(text1,(WIDTH//2 - 170,200))
        screen.blit(text2,(WIDTH//2 - 70,300))
        screen.blit(text3,(WIDTH//2 - 120,350))

        pygame.display.update()


    def draw_win(self):

        screen.fill((0,0,0))

        font_big = pygame.font.SysFont(None,72)
        font_small = pygame.font.SysFont(None,36)

        text1 = font_big.render("YOU WIN!",True,GREEN)
        text2 = font_small.render(f"Final Score : {self.score}",True,WHITE)
        text3 = font_small.render("Press R to Restart",True,WHITE)

        screen.blit(text1,(WIDTH//2 - 150,200))
        screen.blit(text2,(WIDTH//2 - 100,300))
        screen.blit(text3,(WIDTH//2 - 120,350))

        pygame.display.update()

game = Game()
running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if game.game_over or game.win:

                if event.key == pygame.K_r:
                    game = Game()

            else:

                game.player.move(event.key)
    if game.game_over:
        game.draw_game_over()
    elif game.win:
        game.draw_win()
    else:
        game.update()
        game.draw()



pygame.quit()