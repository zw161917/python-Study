import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
#直方图反向投影

# 二进制直方图
def hist2d_demo(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,256])
    # cv.imshow("hist2d",hist)
    plt.imshow(hist,interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()

# 直方图反向衍射
def back_projection_demo():
    image1 = cv.imread("D:/opencvwen/zhishe.PNG")
    image2 = cv.imread("D:/opencvwen/tizhuqiu.PNG")
    roi_hsv = cv.cvtColor(image1,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(image2, cv.COLOR_BGR2HSV)
    cv.imshow("input image1", image1)
    cv.imshow("input image2", image2)
    roisist = cv.calcHist([roi_hsv],[0,1],None,[32,32],[0,180,0,256])
    cv.normalize(roisist,roisist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roisist,[0,180,0,256],1)
    cv.imshow("cBackProject",dst)


print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/demo.PNG")
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image",src)

back_projection_demo()

cv.waitKey(0)

cv.destroyAllWindows()