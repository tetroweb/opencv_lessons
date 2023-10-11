#contour detection
import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("shape.jpg",0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50 , 200)
cv2.imshow("Edged",edged)



cv2.waitKey(3000)
cv2.destroyAllWindows()