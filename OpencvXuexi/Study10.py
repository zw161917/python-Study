import cv2 as cv
import numpy as np

# 直方图均衡化(对比度增强)
def equalHist_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo",dst)

# 局部直方图均衡化(对比度增强)
def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clash = cv.createCLAHE(clipLimit=5.0,tileGridSize=(8,8))
    dst = clash.apply(gray)
    cv.imshow("equalHist_demo", dst)

# 直方图比较
def create_rgb_hist(image):
    h,w,c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):

            b = image[row,col,0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 +np.int(g/bsize)*16 + np.int(r/bsize)
            rgbHist[np.int(index),0] = rgbHist[np.int(index),0] + 1
    return rgbHist

def hist_compare(image1,image2):
    hist1 = create_rgb_hist(image1)
    hist2 = create_rgb_hist(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)#巴氏距离（值越大相识度越小）（0—1之间）
    match2 = cv.compareHist(hist1,hist2,cv.HISTCMP_CORREL)#相关性（值越大相似度越高）（0—1之间） 
    match3 = cv.compareHist(hist1,hist2,cv.HISTCMP_CHISQR)#卡方（值越小相似度越高）
    print("巴氏距离: %s , 相关性: %s , 卡方: %s"%(match1,match2,match3))

print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/mili.PNG")
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image",src)

image1  = cv.imread("D:/opencvwen/linux.PNG")
image2  = cv.imread("D:/opencvwen/win.PNG")
cv.imshow("input image1",image1)
cv.imshow("input image2",image2)
hist_compare(image1,image2)
cv.waitKey(0)

cv.destroyAllWindows()