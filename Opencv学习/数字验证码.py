import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract as tess

# 数字验证码识别

def recognize_text():
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV | cv.THRESH_OTSU) #二值化
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, 15)
    cv.imshow("binary-image", binary)
    # 获取结构元素
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    # bin1 = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    # cv.imshow("binary-image",bin1)

    dst = cv.dilate(binary, kernel)  # 腐蚀
    cv.imshow("binary-image2",dst)
    textimage = Image.fromarray(binary)
    text = tess.image_to_string(textimage)
    print("识别结果：",text)

    # 识别
    cv.bitwise_not(dst,dst) #转换为白色背景



print("---------------Hello Python--------------")
src  = cv.imread("D:/opencvwen/yanzheng1.PNG")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

recognize_text()

cv.waitKey(0)

cv.destroyAllWindows()