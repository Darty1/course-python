from pygame import *
from random import *

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
        self.y_speed += 0.25

    def jump(self, y):
        if self.stands_on:
            self.y_speed = y

    def update(self):
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, walls, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        if self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = min(self.rect.left, p.rect.right)
        self.gravitate()




class Wall(sprite.Sprite):
    def __init__(self, x=x_start, y=y_start, width=120, height=120, color=(73, 69, 0)):
        sprite.Sprite.__init__(self)
        self.image = Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


display.set_caption("Arcada")
window = display.set_mode((800, 600))
background = transform.scale(image.load('cave.png'), (800, 600))
window.blit(background, (0, 0))
hero = Hero('m1.png')
walls = sprite.Group()
wall1 = Wall(50, 150, 480, 20)
walls.add(wall1)
wall1 = Wall(300, 270, 480, 20)
walls.add(wall1)
wall1 = Wall(50, 400, 480, 20)
walls.add(wall1)
window.blit(hero.image, (hero.rect.x, hero.rect.y))
display.update()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                hero.x_speed -= 5
            if e.key == K_RIGHT:
                hero.x_speed += 5

    hero.update()
    window.blit(background, (0, 0))
    walls.draw(window)
    window.blit(hero.image, (hero.rect.x, hero.rect.y))
    display.update()
    time.delay(50)

