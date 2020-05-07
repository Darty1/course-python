from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from affine import Affine
import string
import cv2
import numpy as np
import easygui


def inp():
    n = int(input("""
        1. чтение изображения
        2. вывод изображения на экран
        3. преобразование из RGB в Gray
        4. аффинные преобразования (перемещение; масштабирование; поворот; сдвиг)
        5. вывод преобразованного изображения на экран
        6. вывод каждого канала изображения на экран
        7. сохранение преобразованного изображения в заданной директории
        8. сохранение каждого канала изображения в заданной директории
        0. выход
        Выберите пункт: """))
    return n


def loadImage():
    global filename
    filename = str(easygui.fileopenbox())
    global im
    im = Image.open(filename)
    return im, filename

def saveImage():
    filename = easygui.filesavebox(msg="Save")
    print(filename)
    im.save(filename+'.jpg')


def viewImage():
    im.show()


def show_im():
    try:
        im.show()
    except NameError:
        print("Open File, please")


def gray():
    try:
        draw = ImageDraw.Draw(im)
    except NameError:
        print("Open file, please")
    else:
        width = im.size[0]
        height = im.size[1]
        pix = im.load()
        for i in range(width):
            for j in range(height):
                a = pix[i, j][0]
                b = pix[i, j][1]
                c = pix[i, j][2]
                S = (a + b + c) // 3
                draw.point((i, j), (S, S, S))
        del draw


def show_chanel():
    src = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    print(src.shape)
    red_channel = src[:, :, 2]
    red_img = np.zeros(src.shape)
    red_img[:, :, 2] = red_channel
    cv2.imwrite('r.jpg', red_img)
    global r
    r = Image.open('r.jpg')
    r.show()
    green_channel = src[:, :, 1]
    green_img = np.zeros(src.shape)
    green_img[:, :, 1] = green_channel
    cv2.imwrite('g.jpg', green_img)
    global g
    g = Image.open('g.jpg')
    g.show()
    blue_channel = src[:, :, 0]
    blue_img = np.zeros(src.shape)
    blue_img[:, :, 0] = blue_channel
    cv2.imwrite('b.jpg', blue_img)
    global b
    b = Image.open('b.jpg')
    b.show()

def save_channel():
    filename = easygui.filesavebox(msg="Save")
    r.save(filename+'_r.jpg')
    g.save(filename + '_g.jpg')
    b.save(filename + '_b.jpg')

