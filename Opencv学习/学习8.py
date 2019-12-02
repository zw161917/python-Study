#边缘保留滤波EPF
import cv2 as cv
import numpy as np

# 高斯双边
def bi_demo(image):
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow("bi_demo",dst)

#均值迁移
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,50)
    cv.imshow("bi_demo",dst)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/demo.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

shift_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()