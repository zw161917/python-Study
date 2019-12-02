import cv2 as cv
import numpy as np
    # 分水岭算法
# 基于距离的分水岭分割流程：
#                 输入图像--灰度--二值化--距离变换--寻找种子--生成Marker--分水岭变换--输出图像

def watershed_demo():
    print(src.shape)
    blurre = cv.pyrMeanShiftFiltering(src, 10, 100)  # 去皂
#     groy/binary image
    gray = cv.cvtColor(blurre,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)  # 阈值
    cv.imshow("binary-image", binary)

#     morpholoyp openrottion
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_RECT, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow("mor-otp", sure_bg)

#     距离变换
    dist = cv.distanceTransform(mb,cv.DIST_L2,3)
    dist_output = cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
    dist_output = np.uint8(dist_output)
    cv.imshow("distance-t",dist_output*50)



print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/yuanqian.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

watershed_demo()

cv.waitKey(0)

cv.destroyAllWindows()