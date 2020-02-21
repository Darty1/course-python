from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from affine import Affine
import numpy as np
import string
#import cv2
import numpy as np
n = 9
while n != 0:
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
    if n == 1:
        name = input("File name: ")
        try:
            im = Image.open(name+'.jpg')
        except FileNotFoundError:
            print("File not found")
    if n == 2:
        try:
            im.show()
        except NameError:
            print("Open File, please")
    if n == 3:
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
    if n == 7:
        try:
            name_1 = input("File name: ")
            im.save(name_1)
        except NameError:
            print('Сначала преобразуйте файл')
    if n == 5:
        try:
            im = Image.open(name_1)
            im.show()
        except FileNotFoundError:
            print("File not found")
        except NameError:
            print('Сначала сохраните файл')
    if n == 4:
        a = int(input("""
        Выберите необходимое действие:
        1 - перемещение
        2 - масштабирование
        3 - поворот
        4 - сдвиг 
        """))
        if a == 1:
            p = input("Введите путь к файлу: ")
            try:
                img = plt.imread(p)
            except:
                while plt.imread(p) is FileNotFoundError:
                    p = input("Введите корректный путь к файлу: ")
                img = plt.imread(p)
                img.shape
            finally:
                img_transformed = np.empty((2000, 2000, 4), dtype=np.uint8)
                for i, row in enumerate(img):
                    for j, col in enumerate(row):
                        pixel_data = img[i, j, :]
                        input_coords = np.array([i, j, 1])
                        i_out, j_out, _ = T @ input_coords
                        img_transformed[i_out, j_out, :] = pixel_data

                plt.figure(figsize=(5, 5))
                plt.imshow(img_transformed)
                print("im here")




