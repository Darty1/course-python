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


def a_im_read():
    p = "D:/student_projects/lesson_1/pomi/lab_3/" + input("Input File Name: ") + ".jpg"
    try:
        img = cv2.imread(p, 0)
    except:
        while cv2.imread(p, 0) is FileNotFoundError:
            p = "D:/student_projects/lesson_1/pomi/lab_3/" + input("Input File Name: ") + ".jpg"
    finally:
        cv2.imshow('img_before', img)
        return img


def translation(x, y):
    img = a_im_read()
    rows, cols = img.shape
    M = np.float32([[1, 0, x], [0, 1, y]])
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('img_after', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def rotation(r):
    img = a_im_read()
    rows, cols = img.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), r, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('img_after', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def scalling(fx, fy):
    img = a_im_read()
    img_scaled = cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('Scaling - Skewed Size', img_scaled)
    cv2.waitKey()


def sdvig(x, y):
    img = a_im_read()
    rows, cols = img.shape[:2]
    src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
    dst_points = np.float32([[0, 0], [int(x * (cols - 1)), 0], [int(y * (cols - 1)), rows - 1]])
    affine_matrix = cv2.getAffineTransform(src_points, dst_points)
    img_output = cv2.warpAffine(img, affine_matrix, (cols, rows))
    cv2.imshow('Output', img_output)
    cv2.waitKey()