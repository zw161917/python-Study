import cv2 as cv
import numpy as np

def face_detect_demo(image,a):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY) #灰度图像
    # 极点检测器
    face_detector = cv.CascadeClassifier("D:/opencvwen/opencv-master/data/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces = face_detector.detectMultiScale(gray,1.02,5)

    for x,y,w,h in faces:
        cv.rectangle(image,(x-2,y-2),(x+w+1,y+h+1),(0,0,255),2)

        cropped = image[y+8:y+h-8,x+16:x+w-16]
        # cv.imwrite("D:/opencvwen/renlian/%s_a.jpg"%(a), cropped)
        # print("asdasd：",a)
    cv.imshow("result",image)


print("---------------Hello Python--------------")
# src  = cv.imread("D:/opencvwen/renlian.PNG")
# cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
capture = cv.VideoCapture(0)
# capture = cv.VideoCapture("D:/opencvwen/renlian/yang.mp4")
# cv.namedWindow("result",cv.WINDOW_AUTOSIZE)
# cv.imshow("input image",src)
a = 0
while(True):
    a = a + 1
    ret,frame = capture.read()
    frame = cv.flip(frame,1)
    face_detect_demo(frame,a)
    c = cv.waitKey(10)
    if c == 27:
        break

# face_detect_demo()

cv.waitKey(0)

cv.destroyAllWindows()