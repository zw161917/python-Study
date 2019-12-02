import cv2 as cv
import numpy as np
# 图像梯度
# 一阶导数与Soble算子  用作边缘检测的离散微分算子
# 二阶导数与拉普拉斯算子  会使求导过程变得简单

# Soble算子
def soble_demo(image):
    grad_x = cv.Sobel(image,cv.CV_32F,1,0)
    grad_y = cv.Sobel(image,cv.CV_32F,0,1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient_x",gradx)
    cv.imshow("gradient_y",grady)

    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradxy",gradxy)

# Scharr算子(Soble算子的增强版)
def scharr_demo(image):
    grad_x = cv.Scharr(image,cv.CV_32F,1,0)
    grad_y = cv.Scharr(image,cv.CV_32F,0,1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient_x",gradx)
    cv.imshow("gradient_y",grady)

    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradxy",gradxy)

# 拉普拉斯算子
def lapalian_demo(image):
    # dst = cv.Laplacian(image,cv.CV_32F)
    # lals = cv.convertScaleAbs(dst)
    # 自己定义
    kernel = np.array([[1,1,1],[1,-8,1],[1,1,1]])
    dst = cv.filter2D(image,cv.CV_32F,kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian_demo",lpls)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/demo.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

lapalian_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()