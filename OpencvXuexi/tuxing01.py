import cv2 as cv
import numpy as np
# 对象测量

def measure_object(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    print("threshold value:",ret)
    cv.imshow("binary imag",binary)
    contoures,hireachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contoure in enumerate(contoures):
        area = cv.contourArea(contoure) #得到轮廓
        x,y,w,h = cv.boundingRect(contoure)    #得到轮廓的外接矩形
        rate = min(w,h)/max(w,h)    #宽高比
        print("宽高比：",rate)
        mm = cv.moments(contoure)    #得到几何距
        print(type(mm))
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(image,(np.int(cx),np.int(cy)),2,(0,255,255),-1)   #在原图上绘制
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2) #根据轮廓绘制外接矩形
        print("contour area",area)
    cv.imshow("measure-contours",image)

#图形检测
def tuxing_object(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
    print("threshold value:",ret)
    cv.imshow("binary imag",binary)
    dst = cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    contoures,hireachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    a=0
    b=0
    c=0
    for i,contoure in enumerate(contoures):
        area = cv.contourArea(contoure) #得到轮廓
        x,y,w,h = cv.boundingRect(contoure)    #得到轮廓的外接矩形
        rate = min(w,h)/max(w,h)    #宽高比
        print("宽高比：",rate)
        mm = cv.moments(contoure)    #得到几何距
        print(type(mm))
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(dst,(np.int(cx),np.int(cy)),2,(0,255,255),-1)   #在原图上绘制
        # cv.rectangle(dst,(x,y),(x+w,y+h),(0,0,255),2) #根据轮廓绘制外接矩形
        print("contour area",area)
        approx = cv.approxPolyDP(contoure,4,True)
        print(approx.shape)
        if approx.shape[0] > 6:
            cv.drawContours(dst,contoures,i,(0,255,0),2)
            a = a+1
        if approx.shape[0] == 3:
            cv.drawContours(dst,contoures,i,(0,0,255),2)
            b = b + 1
        if approx.shape[0] == 4:
            cv.drawContours(dst,contoures,i,(255,0,0),2)
            c = c + 1
    print("圆的个数：%s，三角形的个数：%s，矩形的个数：%s"%(a,b,c))
    cv.imshow("measure-contours",dst)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/tuyanse2.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

tuxing_object(src)

cv.waitKey(0)

cv.destroyAllWindows()