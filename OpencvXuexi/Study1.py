import cv2 as cv
import numpy as np


def get_image_info(image):
    print(type(image))
    print(image.shape)  #高和宽以及通道数
    print(image.size)   #像素多少
    print(image.dtype)  #字节位数占多少
    #print(image)
    # pixce_data = np.arange([image])
    #     # print(pixce_data)


#开启摄像头函数
def voideo_demo():
    capture = cv.VideoCapture(0)
    while(True):
            ret,frme = capture.read()
            frme = cv.flip(frme,1) #将摄像头颠倒过来
            cv.imshow("vishexiangtou",frme)
            c = cv.waitKey(50)
            if(c == 27):
                break

src = cv.imread("img4.PNG")
#cv.WINDOW_AUTOSIZE
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#显示
cv.imshow("input image",src)
# cv.imwrite("fuzhi1.PNG",src)
get_image_info(src)
# voideo_demo()
cv.waitKey(0)#等待下一个用户的炒作
cv.destroyAllWindows()#释放所有的内存



