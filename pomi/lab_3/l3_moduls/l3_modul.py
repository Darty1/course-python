from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from affine import Affine
import string


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


def read_im():
    name = "D:/student_projects/lesson_1/pomi/lab_3/" + input("Input File Name: ") + ".jpg"
    print(name)
    try:
        im = Image.open(open(name, 'rb'))
    except FileNotFoundError:
        print("File not found")

    return im


def show_im(im):
    try:
        im.show()
    except NameError:
        print("Open File, please")


def gray(im):
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
    return im

