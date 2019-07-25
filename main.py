# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:48:16 2019

@author: sunbo
"""

import cv2

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.png")
img3 = cv2.imread("3.png")
Lenna = cv2.imread('Lenna.png')


# RGB 图像转换为 灰度图像
img1_gray = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
img3_gray = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

def run_algorithm(img_gray1, img_gray2, img_gray3, algo_type):
    
    if algo_type == 'Laplacian':    #Laplacian算子处理后的图像的平均灰度值，值越大，代表图像越清晰
        # 灰度图像 ——> 梯度图像
        img1_ret = cv2.Laplacian(img1_gray, cv2.CV_16U)
        img2_ret = cv2.Laplacian(img2_gray, cv2.CV_16U)
        img3_ret = cv2.Laplacian(img3_gray, cv2.CV_16U)
        
        # 图像的平均灰度
        meanValue1 = cv2.mean(img1_ret)[0]
        meanValue2 = cv2.mean(img2_ret)[0]
        meanValue3 = cv2.mean(img3_ret)[0]
        
    elif algo_type == 'Sobel':  #Sobel算子处理后的图像的平均灰度值，值越大，代表图像越清晰
        img1_ret = cv2.Sobel(img1_gray, cv2.CV_16U, 1, 1)
        img2_ret = cv2.Sobel(img2_gray, cv2.CV_16U, 1, 1)
        img3_ret = cv2.Sobel(img3_gray, cv2.CV_16U, 1, 1)
        
        # 图像的平均灰度
        meanValue1 = cv2.mean(img1_ret)[0]
        meanValue2 = cv2.mean(img2_ret)[0]
        meanValue3 = cv2.mean(img3_ret)[0]
        
    elif algo_type == 'Variance':   #方差越大，表示清晰度越好
        global img1_meanValue,img1_meanStdValue
        (img1_meanValue, img1_meanStdValue) = cv2.meanStdDev(img1_gray, cv2.CV_16U)
        (img2_meanValue, img2_meanStdValue) = cv2.meanStdDev(img2_gray, cv2.CV_16U)
        (img3_meanValue, img3_meanStdValue) = cv2.meanStdDev(img3_gray, cv2.CV_16U)
        
        meanValue1 = img1_meanStdValue[0][0]
        meanValue2 = img2_meanStdValue[0][0]
        meanValue3 = img3_meanStdValue[0][0]

    print('value1: ', meanValue1)
    print('value2: ', meanValue2)
    print('value3: ', meanValue3)
    
    
#run_algorithm(img1_gray, img2_gray, img3_gray, 'Sobel')

cv2.imshow('1', img1)
cv2.imshow('2', img2)

key1Flag = True;
key2Flag = True;

while key1Flag or key2Flag:
    key = cv2.waitKey(0)
    if key == 49 and key1Flag:
        cv2.destroyWindow('1')
        key1Flag = False
    elif key == 50 and key2Flag:
        cv2.destroyWindow('2')
        key2Flag = False
    else:
        cv2.namedWindow(str(key), cv2.WINDOW_NORMAL)
        cv2.imshow(str(key),Lenna)
        print(key)

cv2.destroyAllWindows()

Lenna_gray = cv2.cvtColor(Lenna, cv2.COLOR_RGB2GRAY)
cv2.imwrite('Lenna_Gray.png', Lenna_gray)