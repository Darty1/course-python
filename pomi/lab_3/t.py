import cv2
import numpy as np

#read image
src = cv2.imread('Cat.jpg', cv2.IMREAD_UNCHANGED)
print(src.shape)
red_channel = src[:, :, 0]
red_img = np.zeros(src.shape)
red_img[:, :, 0] = red_channel
cv2.imwrite('r.png', red_img)

