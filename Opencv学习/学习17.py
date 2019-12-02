import cv2 as cv
import numpy as np
# Canny边缘提取（看妮）
'''
Canny边缘检测一共分为五步
    1.高斯模糊--GaussianBlur
    2.灰度转换--cvtColor
    3.计算梯度--Sobel/Scharr
    4.非最大信号抑制
    5.高低阈值输出二值图像
'''

def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    # x Gradient(x方向的梯度)
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    # y Grodient
    ygrad = cv.Sobel(gray,cv.CV_16SC1,0,1)
    #edge(边缘)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    cv.imshow("Canny Edge",edge_output)

    #设为彩色
    dst = cv.bitwise_and(image,image,mask=edge_output)
    cv.imshow("Color Edge",dst)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/tuyanse2.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

edge_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()