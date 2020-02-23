from pygame import *

window = display.set_mode((700, 500))
display.set_caption("First game")


## Background
# window.fill((255, 255, 255))
img1 = transform.scale(image.load('kitty/shutterstock_1220361823-[Converted]-2.png'), (100, 100))
background = transform.scale(image.load("fields.png"), (700, 500))


## Draw sprite:
# img1 = draw.rect(window, (0, 0, 255), (5, 435, 40, 60))
# draw.aaline(window, (255, 0, 0), [0, 0], [200, 200])
# draw.ellipse(window, (0, 255, 255), (300, 300, 100, 200))
# window.blit(draw.rect(window, (0, 0, 255), (5, 435, 40, 60)), (0, 0))
window.blit(background, (0, 0))
display.update()

run = True
x2 = 0
y2 = 0
speed = 10
while run:
    time.delay(50)
    for e in event.get(): # List of events
        if e.type == QUIT:
            exit()
        window.blit(background, (0, 0))
        window.blit(img1, (x2, y2))
        keys = key.get_pressed()
        if keys[K_LEFT] and x2 > 5:
            x2 -= speed
        if keys[K_RIGHT] and x2 < 595:
            x2 += speed
        if keys[K_UP] and y2 > 5:
            y2 -= speed
        if keys[K_DOWN] and y2 < 395:
            y2 += speed
        display.update()

        # if e.type == KEYDOWN: # Key is down
        #     if e.key == K_RIGHT:
        #         x += 10
        #     if e.key == K_LEFT:
        #         x -= 10
        #     if e.key == K_UP:
        #         y -= 10
        #     if e.key == K_DOWN:
        #         y += 10
    # window.blit(background, (0, 0)) # basckground
    # window.blit(img1, (x, y)) # sprite
    # display.update()
time.delay(5000)