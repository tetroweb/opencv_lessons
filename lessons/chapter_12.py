#edge detection
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("img.png",0)
plt.figure(),plt.imshow(img,cmap = "gray"),plt.axis("off"),plt.title("original")

edges = cv2.Canny(img, threshold1 = 0 , threshold2 = 255)
plt.figure(),plt.imshow(edges,cmap = "gray"),plt.axis("off"),plt.title("edges")
plt.show()

med_val = np.median(img)
print(med_val)

low = int(max(0,(1-0.33))*med_val)
high= int(min(255,(1+0.33))*med_val)

edges2 = cv2.Canny(img, threshold1 = low , threshold2 = high)
plt.figure(),plt.imshow(edges2,cmap = "gray"),plt.axis("off"),plt.title("edges2")
plt.show()

#blur 
blured_img = cv2.blur(img ,ksize=(5,5))
plt.figure(),plt.imshow(blured_img,cmap = "gray"),plt.axis("off"),plt.title("blured")
plt.show()


med_val = np.median(blured_img)
print(med_val)

low = int(max(0,(1-0.33))*med_val)
high= int(min(255,(1+0.33))*med_val)

edges2 = cv2.Canny(blured_img , threshold1 = low , threshold2 = high)
plt.figure(),plt.imshow(edges2,cmap = "gray"),plt.axis("off"),plt.title("edges2")
plt.show()
