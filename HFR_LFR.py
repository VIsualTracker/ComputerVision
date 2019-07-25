# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:13:27 2019

@author: sunbo
"""

import cv2
import numpy as np
from scipy import ndimage

HFR_K3 = np.array([[0, -1, 0],
         [-1, 4, -1],
         [0, -1, 0]])

HFR_K5 = np.array([[-1, -1, -1, -1, -1],
                   [-1, 1, 2, 1, -1],
                   [-1, 2, 4, 2, -1],
                   [-1, 1, 2, 1, -1],
                   [-1, -1, -1, -1, -1]])

# 获得灰度图像
img = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

img_k3 = ndimage.convolve(img, HFR_K3)
img_k5 = ndimage.convolve(img, HFR_K5)

img_blur = cv2.GaussianBlur(img, (11,11), 0)
img_self = img - img_blur

cv2.imshow('ori img', img)
cv2.imshow('3x3 HFR', img_k3)
cv2.imshow('5x5 HFR', img_k5)
cv2.imshow('Self HFR', img_self)

cv2.waitKey(0)
cv2.destroyAllWindows()