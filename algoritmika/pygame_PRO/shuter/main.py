from pygame import *
from random import *


font.init()
font = font.Font(None, 36)
score = 0
lost = 0
max_lost = 5
max_score = 10
class SpriteFamily(sprite.Sprite):  # класс-родитель всех спрайтов
    def __init__(self, img, x, y, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (50, 50))  # загрузка картинки
        self.speed = speed  # скорость (количество пройденных пикселей за шаг)
        self.rect = self.image.get_rect()  # прямоугольник вокруг картинки
        self.rect.x = x  # начальная координата х
        self.rect.y = y  # начальная координата у

    def show(self):  # функция рисования спрайта на экране
        window.blit(self.image, (self.rect.x, self.rect.y))


class SpriteHero(SpriteFamily):  # класс спрайта героя, наследуемый от класса-родителя
    def go(self):  # функция управления кнопками
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx-7, self.rect.top, -15)
        bullet.image = transform.scale(image.load('bullet.png'), (15, 20))
        bullets.add(bullet)

class SpriteEnemy(SpriteFamily):  # класс спрайта врага
    def update(self):  # функция автоматического хождения
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 620)
            self.rect.y = 0
            lost += 1

class Bullet(SpriteFamily):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
def begin():
    global window
    window = display.set_mode((700, 500))  # создание окна и установка его размеров
    display.set_caption("Shuter228")  # установка названия окна
    ## Background
    global background
    background = transform.scale(image.load('galaxy.jpg'), (700, 500))  # трансформирование картинки
    global hero
    hero = SpriteHero('rocket.png', 340, 440, 10)  # создание объекта героя (путь к картинке, х, у, скорость)
    global monsters
    monsters = sprite.Group()
    for i in range(1, 6):
        monster = SpriteEnemy('ufo.png', randint(80, 620), -40, randint(1, 5))
        monsters.add(monster)
    global bullets
    bullets = sprite.Group()
    global hearts
    hearts = sprite.Group()
    x_h = 500
    y_h = 40
    for i in range(1, 4):
        heart = SpriteFamily('heart.png', x_h, y_h, 0)
        hearts.add(heart)
        x_h += 50
    global finish
    finish = False
begin()
# Основной цикл игры:
run = True  # флаг сбрасывается кнопкой закрытия окна
while run:
    time.delay(50)  # задержка 0.05s, чтобы было плавнее
    for e in event.get():  # отлавливаем все события
        if e.type == QUIT:  # если нажат крестик на окне
            run = False  # цикл заканчивается
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
            if e.key == K_RETURN:
                begin()
                lost = 0
                score = 0
                # for i in range(1, 6):
                #     monsters[i].rect.x = randint(80, 620)
                #     monsters[i].rect.y = -40
    if not finish:
        window.blit(background, (0, 0))  # закрашивание экрана картинкой
        text_lose = font.render("Пропущено: "+str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        text_score = font.render("Убито: " + str(score), 1, (255, 255, 255))
        window.blit(text_score, (10, 20))
        hero.go()  # хождение героя
        hero.show()  # отрисовка героя
        monsters.update()  # обновление координаты НЛО
        bullets.update()
        hearts.draw(window)
        monsters.draw(window)  # рисование НЛО на окно
        bullets.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score += 1
            print('score = ', score)
            monster = SpriteEnemy('ufo.png', randint(80, 620), -40, randint(5, 10))
            monsters.add(monster)
        if sprite.spritecollide(hero, monsters, False) or lost >= max_lost:
            finish = True
            window.fill((255, 255, 255))
            img = image.load('game-over.png')
            window.blit(transform.scale(img, (700, 500)), (0, 0))
            text_game_over= font.render("Enter - начать заново", 1, (0, 0, 0))
            window.blit(text_game_over, (310, 360))
        if score >= max_score:
            img = image.load('thumb.jpg')
            window.blit(transform.scale(img, (700, 500)), (0, 0))
            text_game_over = font.render("Enter - начать заново", 1, (0, 0, 0))
            window.blit(text_game_over, (50, 360))
    display.update()  # обновление экрана