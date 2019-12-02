import cv2 as cv
import numpy as np

#像素运算#加法
def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)

#像素运算#减法
def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)

#像素运算除法
def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)

#像素运算乘法
def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply_demo",dst)

#像素运算均值
def others(m1,m2):
    h1 = cv.mean(m1)#通道均值
    h2 = cv.mean(m2)
    h1,dev1 = cv.meanStdDev(m1)  # 通道均值和方差
    h2,dev2 = cv.meanStdDev(m2)
    print(h1)
    print(h2)
    print(dev1)
    print(dev2)

#逻辑运算显示非0图像
def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1,m2)#非叠加后都为非0输出
    dst = cv.bitwise_or(m1, m2)#或叠加后输出所有非0

    cv.imshow("logic_demo",dst)

#调整亮度和对比度
def contrast_brightness_demo(image,c,b):
    h,w,ch = image.shape
    blane = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blane,1-c,b)
    cv.imshow("con-bri-demo",dst)

print("---------------Hello Python--------------")
src1  = cv.imread("D:/opencvwen/linux.PNG")
src2  = cv.imread("D:/opencvwen/win.PNG")
print(src1.shape)
print(src2.shape)
#裁剪图片大小
src2 = src2[0:382, 0:516]
print(src2.shape)
cv.namedWindow("input image1",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image1",src1)
cv.imshow("input image2",src2)
contrast_brightness_demo(src2,1.2,10)#调整对比度，亮度
# add_demo(src1,src2)
# subtract_demo(src1,src2)
# divide_demo(src1,src2)
# multiply_demo(src1,src2)
# others(src1,src2)
# logic_demo(src1,src2)

cv.waitKey(0)

cv.destroyAllWindows()