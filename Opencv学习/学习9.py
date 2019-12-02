import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 直方图
def plot_demo(image):
    plt.hist(image.ravel(),256,[0,255])
    plt.show("直方图")

#  图像的直方图
def image_hist(image):
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show("图像的三通道直方图")

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/demo.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

image_hist(src)

cv.waitKey(0)

cv.destroyAllWindows()