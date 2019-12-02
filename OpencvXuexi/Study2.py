import cv2 as cv
import numpy as np


#属性读取
def access_pixels(image):
    print(image.shape);
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]#通道数目
    print("width:%s,height:%s,channels:%s"%(height,width,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow("pixels_dome",image)

#创建新的图像
def create_image():
    #多通道
    '''
    img = np.zeros([400,400,3],np.uint8)
    img[: , : , 2] = np.ones([400,400])*255
    cv.imshow("new image",img)

    #单通道
    img = np.zeros([400,400,1],np.uint8)
    img[:,:,0] = np.ones([400,400])*127
    cv.imshow("new,image",img)
    '''
    n1 = np.ones([3,3],np.uint8)
    n1.fill(122.388)
    print(n1)

def invers(image):
    dst = cv.bitwise_not(image)
    cv.imshow("primage new" ,dst)


src = cv.imread("juxing2.PNG") #blue,green,red
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)#显示
cv.imshow("input image",src)
t1 = cv.getTickCount()
# access_pixels(src)
create_image()
# invers(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency();
print("time:%s ms"%(time*1000))
cv.waitKey(0)#等待下一个用户的炒作
cv.destroyAllWindows()#释放所有的内存