import cv2
import imutils
import numpy as np
def Extraction(OrigImg,image):
    Edge=cv2.findContours(image.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    Edge=imutils.grab_contours(Edge)

    Blur=cv2.GaussianBlur(image,(3,3),0)
    mask=np.zeros(Blur.shape,dtype="uint8")
    cv2.drawContours(mask,Edge,-1,255,-1)

    (x,y,w,h)=cv2.boundingRect(mask)

    #(x,y,w,h)=cv2.boundingRect(c)
    imageROI = OrigImg[y:y + h, x:x + w]
    maskROI = mask[y:y + h, x:x + w]
    imageROI = cv2.bitwise_and(imageROI, imageROI,
                               mask=maskROI)
    cv2.imshow("Extracted",imageROI)