from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from affine import Affine
import string
from pomi.lab_3.l3_moduls.l3_modul import *
from pomi.lab_3.l3_moduls.aff_modul import *
#import cv2
import numpy as np
n = 9
while n != 0:
    n = inp()
    if n == 1:
        im = read_im()
    if n == 2:
        show_im(im)
    if n == 3:
        gray(im)

    if n == 4:
        a = a_inp()
        if a == 1:
            translation()
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





