from pygame import *
from random import *

mixer.init()
mixer.music.load('boom.mp3')
font.init()
font = font.Font(None, 36)
lost = 0
score = 0
max_lost = 3
max_score = 10
hero_lives = 3
class SpriteFamily(sprite.Sprite): #класс-родитель всех спрайтов
    def __init__ (self, img, x, y, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (50, 50)) #загрузка картинки
        self.speed = speed #скорость (количество пройденных пикселей за шаг)
        self.rect = self.image.get_rect() #прямоугольник вокруг картинки
        self.rect.x = x #начальная координата х
        self.rect.y = y #начальная координата у

    def show(self): #функция рисования спрайта на экране
        window.blit(self.image, (self.rect.x, self.rect.y))


class SpriteHero(SpriteFamily): # класс спрайта героя, наследуемый от класса-родителя
    def go(self): # функция управления кнопками
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.x+14, self.rect.top, -15)
        bullet.image = transform.scale(image.load('bullet.png'), (20, 20))
        bullets.add(bullet)
        mixer.music.play(0)


class SpriteEnemy(SpriteFamily): # класс спрайта врага

    def update(self): # функция автоматического хождения
        self.rect.y += self.speed
        global lost
        global hero_lives
        global lives
        global window
        if self.rect.y > 500:
            self.rect.x = randint(80, 620)
            self.rect.y = 0
            lost += 1
            hero_lives -= 1
            lives = sprite.Group()
            x_h = 650
            y_h = 40
            for i in range(1, hero_lives+1):
                live = Lives('heart.png', x_h, y_h, 0)
                lives.add(live)
                x_h -= 50
            window.fill((255, 0, 0))

class Bullet(SpriteFamily):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


class Lives(SpriteFamily):
    def minus(self):
        self.kill()

def begin():
    global window
    window = display.set_mode((700, 500)) #создание окна и установка его размеров
    display.set_caption("Shuter228") # установка названия окна
    ## Background
    global background
    background = transform.scale(image.load('galaxy.jpg'), (700, 500)) #трансформирование картинки
    global hero
    hero = SpriteHero('rocket.png', 340, 440, 10) #создание объекта героя (путь к картинке, х, у, скорость)
    global monsters
    monsters = sprite.Group()
    for i in range(1, 6):
        monster = SpriteEnemy('ufo.png', randint(80, 620), -40, randint(1, 5))
        monsters.add(monster)
    global bullets
    bullets = sprite.Group()
    global lives
    lives = sprite.Group()
    x_h = 650
    y_h = 40
    for i in range(1, 4):
        live = Lives('heart.png', x_h, y_h, 0)
        lives.add(live)
        x_h -= 50
    global finish
    finish = False
begin()
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    time.delay(50) #задержка 0.05s, чтобы было плавнее
    for e in event.get(): #отлавливаем все события
        if e.type == QUIT: #если нажат крестик на окне
            run = False  #цикл заканчивается
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
            if e.key == K_RETURN:
                finish = False
                score = 0
                lost = 0
                hero_lives = 3
                begin()
    if not finish:
        window.blit(background, (0, 0))  # закрашивание экрана картинкой
        text_lose = font.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        text_score = font.render("Убито: " + str(score), 1, (255, 255, 255))
        window.blit(text_score, (10, 20))
        text_lives = font.render("Жизни: "+str(hero_lives), 1, (255, 255, 255))
        window.blit(text_lives, (10, 80))
        hero.go() #хождение героя
        hero.show() #отрисовка героя
        monsters.update() #обновление координаты НЛО
        monsters.draw(window) #рисование НЛО на окно
        bullets.update()
        bullets.draw(window)
        lives.update()
        lives.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            boom_img = image.load('boom.png')
            window.blit(transform.scale(boom_img, (50, 50)), (c.rect.x, c.rect.y))
            monster = SpriteEnemy('ufo.png', randint(80, 620), -40, randint(1, 5))
            monsters.add(monster)
            score += 1
        if sprite.spritecollide(hero, monsters, False) or lost >= max_lost:
            finish = True
            window.fill((255, 255, 255))
            img = image.load('game-over.png')
            window.blit(transform.scale(img, (700, 500)), (0,0))
            lose_text = font.render("Enter - Начать заново", 1, (0, 0, 0))
            window.blit(lose_text, (270, 380))
        if score >= max_score:
            finish= True
            img = image.load('thumb.jpg')
            window.blit(transform.scale(img, (700, 500)), (0, 0))
            win_text = font.render("Enter - Начать заново", 1, (0, 0, 0))
            window.blit(win_text, (80, 400))
    display.update() #обновление экрана