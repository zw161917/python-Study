import cv2 as cv
import numpy as np
# 形态学（图像的开闭操作）
# 开操作：基于膨胀与腐蚀操作组合形成的，主要用于二值化分析中，灰度图像亦可。
# 开操作 = 腐蚀 + 膨胀，输入图像 + 结构元素  作用：可以帮助我们消除图像中小的干扰区域（照点）
# 闭操作：基于膨胀与腐蚀操作组合形成的，主要用于二值化分析中，灰度图像亦可。
# 闭操作 = 膨胀 + 腐蚀，输入图像 + 结构元素  作用：可以填充小的封闭区域
# 综合作用：可以提取水平或者垂直直线

# 开
def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))  #得到结构元素（这里得到矩形的）
    binary = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("open_demo",binary)

# 闭
def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(15,15))  #得到结构元素（这里得到矩形的）
    binary = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("open_demo",binary)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/kaibi.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

close_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()