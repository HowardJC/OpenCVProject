from .extraction import Extraction
from .Extraction.DocumentDetection import DocumentExtract
from .Extraction.Zoom import Zooming
import cv2
class Operations():

    Extract=Extraction

    @staticmethod
    def Extraction(image):
        image,points=DocumentExtract(image)
        Zoomed=Zooming(image,points)
        return Zoomed