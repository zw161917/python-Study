import cv2 as cv
import numpy as np
# 轮廓发现：
'''
是基于图像边缘提取的基础寻找对象轮廓的方法。
所以边缘提取的阈值选定会影响最终轮廓发现结果
'''
# 对边缘操作
def contours_demo(image):
    '''
    dst = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU) #二值化
    cv.imshow("binary image",binary)
    '''
    binary = edge_demo(image)
    # 查找轮廓
    # 返回轮廓改变，轮廓的存放，层次的信息
    contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
        print(i)
    cv.imshow("detect contours",image)

def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    # x Gradient(x方向的梯度)
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    # y Grodient
    ygrad = cv.Sobel(gray,cv.CV_16SC1,0,1)
    #edge(边缘)
    edge_output = cv.Canny(xgrad,ygrad,360,400)
    cv.imshow("Canny Edge",edge_output)

    return edge_output


print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/tuyanse2.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

contours_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()