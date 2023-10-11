#perspective
import cv2
import numpy as np


#
img = cv2.imread("img.png")
cv2.imshow("original image",img)

width = 400
height = 500

#points which applicate  perspective
pts1 = np.float32([[230,1],[1,472],[540,150],[338,617]])

#points which get perspective
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

#
img_output =cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("perspective",img_output)

cv2.waitKey(0) &0XFF
cv2.destroyAllWindows()