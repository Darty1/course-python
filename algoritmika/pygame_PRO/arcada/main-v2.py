from pygame import *
from random import *

font.init()
font = font.Font(None, 72)
x_start = 20
y_start = 10


class Hero(sprite.Sprite):
    def __init__(self, img, x_speed=0, y_speed=0, x=x_start, y=y_start, width=120, height=120):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.stands_on = False

    def gravitate(self):
        self.y_speed += 0.5

    def update(self):
        self.rect.x += self.x_speed
        platforms_collide = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for p in platforms_collide:
                self.rect.right = min(self.rect.right, p.rect.left)
        if self.x_speed < 0:
            for p in platforms_collide:
                self.rect.left = min(self.rect.left, p.rect.right)
        self.gravitate()
        self.rect.y += self.y_speed
        platforms_collide = sprite.spritecollide(self, walls, False)
        if self.y_speed > 0:
            for p in platforms_collide:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
                    self.stands_on = p
        if self.y_speed < 0:
            self.stands_on = False
            for p in platforms_collide:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)


class Wall(sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=(77, 52, 0)):
        sprite.Sprite.__init__(self)
        self.image = Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(sprite.Sprite):
    def __init__(self, img, x=20, y=0, width=100, height=100):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += randint(-5, 5)


class Bullet(sprite.Sprite):

    def __init__(self, img, x, y, width=50, height=50):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x += 10

class FinalSprite(sprite.Sprite):
    def __init__(self, img, x, y, width=100, height=100):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

window = display.set_mode((800, 600))
display.set_caption('Arcada')
backround = transform.scale(image.load('cave.png'), (800, 600))
window.blit(backround, (0, 0))
hero = Hero('m1.png')
princess = FinalSprite('princess.png', 500, 270)
enemies = sprite.Group()
enemy = Enemy('enemy.png', 350, 270)
enemies.add(enemy)
walls = sprite.Group()
w = Wall(50, 150, 480, 20)
walls.add(w)
w = Wall(700, 50, 50, 360)
walls.add(w)
w = Wall(350, 380, 640, 20)
walls.add(w)
w = Wall(-200, 590, 160, 20)
walls.add(w)
walls.draw(window)
window.blit(hero.image, (hero.rect.x, hero.rect.y))
display.update()
run = True
finish = False
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                hero.x_speed -= 10
            if e.key == K_RIGHT:
                hero.x_speed += 10
        if e.type == KEYUP:
            if e.key == K_LEFT:
                hero.x_speed = 0
            if e.key == K_RIGHT:
                hero.x_speed = 0
    if not finish:
        hero.update()
        enemies.update()
        window.blit(backround, (0, 0))
        walls.draw(window)
        enemies.draw(window)
        window.blit(hero.image, (hero.rect.x, hero.rect.y))
        window.blit(princess.image, (princess.rect.x, princess.rect.y))
        if sprite.spritecollide(hero, enemies, False):
            finish = True
            window.fill((255, 255, 255))
            text = font.render("GAME OVER", 1, (255, 0, 0))
            window.blit(text, (300, 300))
    display.update()
