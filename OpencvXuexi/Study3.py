import cv2 as cv
import numpy as np

# 色彩空间相互转换API
def color_space_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    ycrcb = cv.cvtColor(image,cv.COLOR_BGR2YCrCb)
    cv.imshow("ycrcb",ycrcb)
# 视频播放
def extrace_object_demo():
    print("asda")
    capture = cv.VideoCapture("D:/opencvwen/python_shipin.mp4")
    while(True):
        ret,frame = capture.read()
        if ret==False:
            break;
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        # 对绿色进行二值化
        lower_hsv = np.array([37,43,46])#先进性设置hsv的最小值
        upper_hsv = np.array([77,255,255])#设置hsv的最大值
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        dst = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow("video",frame)#正常播放
        cv.imshow("mask",dst)#二值化后播放
        c= cv.waitKey(40)
        if c == 27:
            break;

print("---------------Hello Python--------------")
src  = cv.imread("juxing1.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imwrite("D:/opencvwen/s_a.jpg", src)
# cv.imshow("input image",src)

# b,g,r = cv.split(src)#通道分离
# cv.imshow("blue",b)
# cv.imshow("green",g)
# cv.imshow("red",r)
# extrace_object_demo()
# src[:,:,0] = 0#通道赋值
#
# src = cv.merge([b,g,r])#通道合并
# color_space_demo(src)
# cv.imshow("changed image",src)
cv.waitKey(0)

cv.destroyAllWindows()