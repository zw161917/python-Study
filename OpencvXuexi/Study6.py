import cv2 as cv
import numpy as np

# 均值模糊
def blur_demo(image):
    dst = cv.medianBlur(image,(5,5))
    cv.imshow("blur_demo",dst)

# 中值模糊（消除椒盐噪声）
def median_demo(image):
    dst = cv.blur(image,5)
    cv.imshow("blur_demo",dst)

# 自定义模糊
def custom_demo(image):
    kernel = np.ones([5,5],np.float32)/25
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)#锐化
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("blur_demo",dst)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/demo.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
custom_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()