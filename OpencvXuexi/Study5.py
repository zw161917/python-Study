import cv2 as cv
import numpy as np
# ROI与泛红填充

def fill_color_demo(image):
    copyimg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyimg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("input image",copyimg)

# 二值填充
def fill_binary():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300, : ] = 255
    cv.imshow("input image", image)

    mask = np.ones([402,402,1],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary",image)


print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/demo.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

# ROI操作
'''
face = src[50:250,100:300]
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[50:250,100:300] = backface
cv.imshow("face",src)
'''

# 泛红填充
fill_color_demo(src)

fill_binary()

cv.waitKey(0)

cv.destroyAllWindows()