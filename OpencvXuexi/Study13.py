import cv2 as cv
import numpy as np
# 图像二值化

#全局阈值
def threshold_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)#图像灰度化
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)#二值化
    #ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)  # 反向二值化
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)  # 截断二值化（大于127的为0）
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)  # 截断二值化（小于127的为0）
    print("thresho;d value %s"%ret)
    cv.imshow("binsry",binary)

# 局部阈值
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 图像灰度化
    binary = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,25,10)#谁民事局部
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)#谁民事局部(效果更好)
    cv.imshow("binsry", binary)

#自己计算均值
def custom_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    h,w = gray.shape[:2]
    # m = np.reshape(gray,[1,w+h])
    mean = gray.sum() / (w*h)
    print("mean : ",mean)
    ret,binary = cv.threshold(gray,mean,255,cv.THRESH_BINARY)
    cv.imshow("binary",binary)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/demo.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

custom_threshold(src)

cv.waitKey(0)

cv.destroyAllWindows()