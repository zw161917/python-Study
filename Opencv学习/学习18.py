import cv2 as cv
import numpy as np
# 直线检测（霍夫直线变换）
'''
霍夫直线变换
    平面空间到极坐标空间转换 
'''

def line_detection(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize=3)
    lines = cv.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        xo = a * rho
        yo = b * rho
        x1 = int(xo*1000*(-b))
        y1 = int(yo*1000*(a))
        x2 = int(xo*1000*(-b))
        y2 = int(yo*1000*(a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("image-lines",image)

# 直接得到线端
def line_detect_possible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, 1, np.pi / 180,100,minLineLength=50,maxLineGap=10)
    for line in lines:
        print(type(line))
        x1,y1,x2,y2 = line[0]
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow("line_detect_possible_demo",image)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/zhixian.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

line_detect_possible_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()