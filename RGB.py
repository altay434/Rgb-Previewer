from re import S
import cv2 as cv
from cv2 import data
import numpy as np
def passing():
    pass
cv.namedWindow("Renk")
cv.resizeWindow("Renk",300,300)

square = np.zeros((300,300,3),dtype=np.uint8)
hsv_square = cv.cvtColor(square,cv.COLOR_BGR2HSV)

cv.createTrackbar("Red","Renk",0,255,passing)
cv.createTrackbar("Green","Renk",0,255,passing)
cv.createTrackbar("Blue","Renk",0,255,passing)



while True:
    red = cv.getTrackbarPos("Red","Renk")
    green = cv.getTrackbarPos("Green","Renk")
    blue = cv.getTrackbarPos("Blue","Renk")
    

    square[:,:,0] = blue
    square[:,:,1] = green
    square[:,:,2] = red

   
    
    cv.imshow("Preview", square)
    

    
    
    if cv.waitKey(1) &0XFF == ord("q"):
        break

cv.destroyAllWindows()
    


