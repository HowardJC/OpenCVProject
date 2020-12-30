import cv2
import imutils
import numpy as np
def resize_color_cvt(image):
    ReSizeImage=imutils.resize(image,height=500)
    ReSizeImage = cv2.GaussianBlur(ReSizeImage, (1,1),0)
    gray=cv2.cvtColor(ReSizeImage,cv2.COLOR_BGR2GRAY)
    return gray

def edge_detection(image):
    ProcessedImage=resize_color_cvt(image)
    image=imutils.resize(image,height=500)
    edge=cv2.Canny(ProcessedImage,75,200)
    kernel = np.ones((20, 20), np.uint8)



    edge=cv2.morphologyEx(edge,cv2.MORPH_CLOSE,kernel)
    contours=cv2.findContours(edge.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=imutils.grab_contours(contours)



    contours=sorted(contours,key=cv2.contourArea,reverse=True)
    for c in contours:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # if our approximated contour has four points, then we
        # can assume that we have found our screen
        if len(approx) == 4:
            contoured = approx
            break

    cv2.drawContours(image,[contoured],-1,(0,255,0),2)
    cv2.imshow("Edged",image)
    cv2.waitKey(0)
    return image,contoured


def DocumentExtract(image):
    Image,EdgePoint=edge_detection(image)
    return Image,EdgePoint.reshape(4,2)