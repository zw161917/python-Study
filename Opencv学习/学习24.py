import cv2 as cv
import numpy as np
# 其他形态学操作（顶帽，黑帽，形态学梯度）
# 顶帽：原图像与操作之间的差值图像
# 黑帽：闭操作图像和源图像的差值图像
# 形态学梯度：基本梯度：用膨胀后的图像减去腐蚀后的图像得到的差值图像
#             内部梯度：用原图像减去腐蚀之后的图像得到差值图像
#             外部图像：用膨胀之后的图像减去原来的图像得到差值图像

# 顶帽（原图-开操作）
def top_hat_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 255
    cv.add(dst,cimage)
    cv.imshow("tophat",dst)

# 黑帽（闭操作-原图）
def blac_khat_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15,15))
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    cv.add(dst, cimage)
    cv.imshow("tophat", dst)

# 基本梯度（膨胀-腐蚀）
def grad_ient_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst = cv.morphologyEx(binary,cv.MORPH_GRADIENT,kernel)
    cv.imshow("tophat",dst)

# 内外梯度（内：原图-腐蚀   外：膨胀-原图）
def gradient2_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    dm = cv.dilate(image, kernel)
    em = cv.erode(image, kernel)
    dst1 = cv.subtract(image, em)  # internal gradient 内部梯度
    dst2 = cv.subtract(dm, image)  # external gradient 外部梯度
    cv.imshow("internal", dst1)
    cv.imshow("external", dst2)

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/kaibi.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

gradient2_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()