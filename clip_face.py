import cv2
import numpy as np
vid = cv2.VideoCapture(0)


def cartoon(img):
    gray=cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    gray = cv2.medianBlur(gray,5)
    edges = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color=cv2.bilateralFilter(img,9,250,250)
    cartoon =cv2.bitwise_and(color,color,mask=edges)
    return cartoon

while True:
    success,img=vid.read()
    out=cartoon(img)
    cv2.imshow("output",out)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
