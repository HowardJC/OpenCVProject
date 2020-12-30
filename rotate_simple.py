import numpy as np
import argparse
import imutils
import cv2
from image_functions import Operations
from color_detection_functions import color_vision

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--image", required=True,
		help="Image Path")
	args = vars(ap.parse_args())
	image=cv2.imread(args['image'])
	#Operations.Extraction(image)
	Zoomed=Operations.Extraction(image)
	color_vision.color_detect(Zoomed)
