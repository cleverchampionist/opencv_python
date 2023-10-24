import numpy as np
import cv2

#load a color image in grayscale
img = cv2.imread('OpenCV_Logo.png', 1)

cv2.imshow('image', img)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite("opencv_logo_GS.png", img)
cv2.destroyAllWindows()