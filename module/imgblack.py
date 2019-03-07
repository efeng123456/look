#-*-coding:utf-8-*-
import cv2
import numpy as np
img = cv2.imread('/Users/fengerqiang/Downloads/xjpic.do.jpg')
rows,cols,channels=img.shape
img=cv2.resize(img,None,fx=0.5,fy=0.5)
rows,cols,channels=img.shape
cv2.imshow('img',img)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue=np.array([78,43,46])
upper_blue=np.array([110,255,255])
mask=cv2.inRange(hsv,lower_blue,upper_blue)
erode=cv2.erode(mask,None,iterations=1)

dilate=cv2.dilate(erode,None,iterations=1)

for i in range(rows):
    for j in range(cols):
        if dilate[i,j]==255:
            img[i,j]=(255,255,255)
cv2.imwrite('/Users/fengerqiang/Downloads/xjpic.do1.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()