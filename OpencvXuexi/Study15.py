import cv2 as cv
import numpy as np
# 图像金字塔原理（高斯金字塔和拉普拉斯金字塔）
# 图片的大小要是2的N次方

# 高斯金字塔  用来向下采样
def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_dewn_"+str(i),dst)
        temp = dst.copy()
    return pyramid_images

# 拉普拉斯金字塔   对图像进行最大程度的还原
def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1,-1,-1):
        if(i-1)<0:
            exand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_images[i - 1], exand)
            cv.imshow("lapalian_demo_" + str[i], lpls)
        else:
            exand = cv.pyrUp(pyramid_images[i],dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1],exand)
            cv.imshow("lapalian_demo_"+str[i],lpls)


print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/demo.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

pyramid_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()