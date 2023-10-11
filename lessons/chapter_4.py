#stack images
import cv2
import numpy as np


#
img = cv2.imread("img.png")
cv2.imshow("image",img)

#hstack 
hstack_img = np.hstack((img,img))
cv2.imshow("hstack",hstack_img)

#vstack 
vstack_img = np.vstack((img,img))
cv2.imshow("vstack",vstack_img)




cv2.waitKey(0) &0XFF
cv2.destroyAllWindows()
