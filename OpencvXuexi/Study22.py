import cv2 as cv
import numpy as np
# 膨胀和腐蚀（形态学最基本的）主要用来处理灰度图像和二值图像

def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  #得到结构元素（这里得到矩形的）
    dst = cv.erode(binary, kernel)   #腐蚀
    cv.imshow("erode_demo", dst)

def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))  #得到结构元素（这里得到矩形的）
    dst = cv.dilate(binary, kernel)   #膨胀
    cv.imshow("erode_demo", dst)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/shuzhi5.PNG")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

dilate_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()