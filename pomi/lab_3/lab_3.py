from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from affine import Affine
import string
from l3_moduls.aff_modul import *
from l3_moduls.l3_modul import *
import cv2
import numpy as np
import easygui
n = 9
while n != 0:
    n = inp()
    if n == 1:
        im = loadImage()
    if n == 2:
        viewImage(im)
    if n == 3:
        gray(im)
    if n == 4:
        a = a_inp()
        if a == 1:
            translation(int(input("x = ")), int(input("y = ")))
        if a == 2:
            scalling(float(input("fx = ")), float(input("fy = ")))
        if a == 3:
            rotation(int(input("gradus = ")))
        if a == 4:
            sdvig(float(input("x = ")), float(input("y = ")))

    if n == 7:
        try:
            saveImage(im)
        except NameError:
            print('Сначала преобразуйте файл')
    if n == 5:
        try:
            viewImage(im)
        except FileNotFoundError:
            print("File not found")
        except NameError:
            print('Сначала сохраните файл')
    if n == 6:
        try:
            im = cv2.imread(n, 0)
        except FileNotFoundError:
            print("File not found")







