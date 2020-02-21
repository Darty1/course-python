from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from affine import Affine
import string
import numpy as np
import cv2


def a_inp():
    a = int(input("""
            Выберите необходимое действие:
            1 - перемещение
            2 - масштабирование
            3 - поворот
            4 - сдвиг 
            """))
    return a


def translation():
    p = "D:/student_projects/lesson_1/pomi/lab_3/" + input("Input File Name: ") + ".jpg"
    try:
        img = cv2.imread(p, 0)
    except:
        while plt.imread(p) is FileNotFoundError:
            p = "D:/student_projects/lesson_1/pomi/lab_3/" + input("Input File Name: ") + ".jpg"
        img = plt.imread(p, 0)

    finally:
        rows, cols = img.shape
        M = np.float32([[1, 0, 100], [0, 1, 50]])
        dst = cv2.warpAffine(img, M, (cols, rows))
        cv2.imshow('img', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
