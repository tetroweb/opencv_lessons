#Histogram
import cv2
import matplotlib.pyplot as plt
import numpy as np

#
img = cv2.imread("img.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("Original image")

print(img.shape)

# img_hist = cv2.calcHist([img] , channels = [0] , mask = None , histSize = [256] , ranges = [0,256])
# print(img_hist.shape)
# plt.figure(),plt.imshow(img_hist),plt.title("Original image")
plt.show()


color = ("b" ,"g" ,"r")
for i,c in enumerate(color):
    hist = cv2.calcHist([img] , channels = [i] , mask = None , histSize = [256] , ranges = [0,256])
    plt.plot(hist , color = c)
    
plt.show()