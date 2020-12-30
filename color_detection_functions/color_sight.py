import cv2
from .config import boundaries
import numpy as np
def color_detect(image):
    for(lower,upper) in boundaries:
        mask=cv2.inRange(image,lower,upper)
        output=cv2.bitwise_and(image,image,mask=mask)
        cv2.imshow("Color",output)
        cv2.waitKey(0)
