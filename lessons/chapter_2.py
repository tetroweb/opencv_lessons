#resize and crop our image
import cv2

#
img = cv2.imread("img.png")
cv2.imshow("demo",img)
print("image size :",img.shape)

#resized
img_resized = cv2.resize(img,(300,300))
cv2.imshow("resize",img_resized)
print("resized image : ", img_resized.shape)

#crop
img_cropped = img[:400,:500] # [height,width]
cv2.imshow("cropped img",img_cropped)
print("crop image : ",img_cropped.shape)

cv2.waitKey(0) &0XFF
cv2.destroyAllWindows()