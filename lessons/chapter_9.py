#MORFOLOJİK OPERASYONLAR 
import cv2
import matplotlib.pyplot as plt
import numpy as np

#
img = cv2.imread("img.png",0)

plt.figure(),plt.imshow(img , cmap = "gray"),plt.axis("off")



#EROZYON -ön plandaki nesnenin sınırlarını aşındırır
kernel = np.ones((3,3),dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(),plt.imshow(result , cmap = "gray"),plt.axis("off")



#GENİŞLEME - ön plandaki nesnenin sınırlarını genişletir - erozyonun tam tersidir
result2 = cv2.dilate(img , kernel , iterations = 1)
plt.figure(),plt.imshow(result2 , cmap = "gray"),plt.axis("off")


#AÇMA - erozyon + genişleme - gürültünün giderilmesinde faydalıdır
whiteNoise = np.random.randint(0,2,size = img.shape[:2])
whiteNoise = whiteNoise * 255
plt.figure(),plt.imshow(whiteNoise , cmap = "gray"),plt.axis("off")

noise_img = whiteNoise + img
plt.figure(),plt.imshow(noise_img , cmap = "gray"),plt.axis("off")


#açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure(),plt.imshow(opening , cmap = "gray"),plt.axis("off"),plt.title("Açilma")


#KAPATMA - genişleme+erozyon - ön plandaki nesnelerin içindeki küçük delikleri veya nesne üzerindeki küçük siyah noktaları kapatmak için kullanışlıdır
blackNoise = np.random.randint(0,2,size = img.shape[:2])
blackNoise = whiteNoise  * -255
black_noise_img = img+blackNoise
black_noise_img[black_noise_img<=-245] =0
plt.figure(),plt.imshow(black_noise_img , cmap = "gray"),plt.axis("off"),plt.title("black noise")

closing = cv2.morphologyEx(black_noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure(),plt.imshow(closing , cmap = "gray"),plt.axis("off"),plt.title("Kapanma")

#MORFOLOJİK GRADYAN - GENİŞLEME - EROZYON - GRADIENT
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure(),plt.imshow(gradient , cmap = "gray"),plt.axis("off"),plt.title("GRADIENT")
plt.show()


