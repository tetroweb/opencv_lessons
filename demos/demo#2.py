import cv2 
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("img.png",0)
plt.figure(),plt.imshow(img , cmap = "gray") , plt.axis("off"),plt.title("Original")
plt.show()

#thresholding

_,threshold = cv2.threshold(img , thresh = 60 , maxval = 255 , type = cv2.THRESH_BINARY)
plt.figure(),plt.imshow(threshold , cmap = "gray"),plt.axis("off"),plt.title("threshold")
plt.show()

#adaptive_thrresholding

adaptiveThreshold = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 , 2)
plt.figure(),plt.imshow(adaptiveThreshold,cmap = "gray"),plt.axis("off"),plt.title("adaptive threshold")
plt.show()

#BLURED
img = cv2.imread("odev1.jpg")
img = cv2.cvtColor(img , cv2.COLOR_RGB2BGR)

mean_blur = cv2.blur(img , ksize=(7,7))
plt.figure(),plt.imshow(mean_blur),plt.axis("off"),plt.title("mean blur")
plt.show()

median_blur = cv2.medianBlur(img , ksize = 7)
plt.figure(),plt.imshow(median_blur),plt.axis("off"),plt.title("median blur")
plt.show()

gaussianBlur = cv2.GaussianBlur(img , ksize=(7,7) , sigmaX = 3)
plt.figure(),plt.imshow(gaussianBlur),plt.axis("off"),plt.title("Gaussian blur")
plt.show()



#salt pepper noise

def saltPepperNoise(img):
    copy_image = np.copy(img)
    s_vs_p = 0.5
    amount = 0.004
    
    number_salt = np.ceil(img.size * amount * s_vs_p ).astype(int)
    coords = [np.random.randint(0,i-1,number_salt) for i in img.shape]
    copy_image[tuple(coords)] = 0 
    
    number_pepper = np.ceil(img.size * amount * (1-s_vs_p)).astype(int)
    coords = [np.random.randint(0,i-1,number_pepper) for i in img.shape]
    copy_image[tuple(coords)] = 1
        
    return copy_image

new_image = saltPepperNoise(img)
plt.figure(),plt.imshow(new_image),plt.axis("off"),plt.title("salt pepper")
plt.show()
    
