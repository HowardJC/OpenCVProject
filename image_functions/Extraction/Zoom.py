import cv2
import numpy as np

def Zooming(image,points):
    points=np.array(points).astype(np.float32)
    Destination=np.shape(image)
    Destination= np.array([[0, 0],   [Destination[0], 0],  [Destination[0], Destination[1]], [0, Destination[1]]], dtype=np.float32)

    Perspective=cv2.getPerspectiveTransform(points,Destination.reshape(4,2))
    warping = cv2.warpPerspective(image,Perspective, (np.shape(image)[0],np.shape(image)[1]))
    cv2.imshow("Warped Image",warping)
    cv2.waitKey(0)
    return warping
