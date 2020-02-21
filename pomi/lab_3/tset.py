from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from affine import Affine
import string
import numpy as np
import cv2

print(1)
p = "D:/student_projects/lesson_1/pomi/lab_3/" + input("Input File Name: ") + ".jpg"
print(1)
img = cv2.imread(p, 0)
print(1)
cv2.imshow("", img)
print(1)
rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
