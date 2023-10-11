#image thresholding
import cv2
import matplotlib.pyplot as plt
import numpy as np

#
img = cv2.imread("img.png",0)

plt.figure()
plt.imshow(img , cmap = "gray")
plt.axis("off")
plt.show()


#thresholding
#(source , sınır değeri bu değerin üstü veya altı threshe uğrayacak demektir , değein üzerindeki pixelleri siyah yap , thresh type'ı )
_ , thresholding = cv2.threshold(img , thresh = 60 , maxval = 60 , type = cv2.THRESH_BINARY) # cv2.THRESH_BINARY_INV

plt.figure()
plt.imshow(thresholding , cmap = "gray")
plt.axis("off")
plt.show()


#adaptive_thresholding
#(img , maxval = eşik değerinin üzerindeyse pixelin alacağı değer , adaptiveMethod = eşikelem yöntemini belirtir gauss ve ortalama ,eşikleme type'ı , blocksize = işlem yapılacak pixelin içine gireceği 11x11 lik matris , c = 11x11 lik matrisin gauss veya ortlama ile sonucunun bulunup bu c sayısının sonuçtan çıkarılması ile eşik değeri oluşur c değeri büyük olursa eşik değeri daha düşük olur. )
thresh_img2 = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 , 2)#(0,5) is more sensitive result
plt.figure()
plt.imshow(thresh_img2 , cmap = "gray")
plt.axis("off")
plt.show()

thresh_img3 = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 , 8)
plt.figure()
plt.imshow(thresh_img3 , cmap = "gray")
plt.axis("off")
plt.show()

thresh_img4 = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 , 15)#(10,20) is less sensitive result
plt.figure()
plt.imshow(thresh_img4 , cmap = "gray")
plt.axis("off")
plt.show()