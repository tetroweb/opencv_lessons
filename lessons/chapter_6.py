#blended  image
import cv2
import matplotlib.pyplot as plt
#
img = cv2.imread("img.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


#gray-scale
gray_img = cv2.imread("img.png",0)
gray_img = cv2.cvtColor(gray_img,cv2.COLOR_BGR2RGB)#matplotlib works rgb color order , cv2 works bgr color order and we convert like this


#show img using matplotlib
plt.figure()
plt.imshow(img)

#show img using matplotlib
plt.figure()
plt.imshow(gray_img)

#blended image = image1 * alpha + image2 * beta
blended = cv2.addWeighted(src1 = img , alpha=0.5 , src2 = gray_img , beta = 0.5 , gamma = 0.5)
plt.figure()
plt.imshow(blended)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()