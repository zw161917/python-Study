import cv2 as cv
import numpy as np
# 超大图像二值化（分块）

def big_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:cw+col]
            ret,dst = cv.threshold(roi,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)#全局阈值
            dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
            gray[row:row+ch,col:cw+col] = dst
            print(np.std(dst),np.mean(dst))
    cv.imwrite("D:/opencvwen/wenzhi2 .png",gray)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/wenzhi.png")
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image",src)

big_binary(src)

cv.waitKey(0)

cv.destroyAllWindows()