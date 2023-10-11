#corner detection
import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread("sudoku.png",0)
img = np.float32(img)
plt.figure(),plt.imshow(img , cmap = "gray"),plt.axis("off"),plt.title("original")



#harris corner detection
dst = cv2.cornerHarris(img , blockSize = 5 , ksize = 3 , k = 0.04)
plt.figure(),plt.imshow(dst , cmap = "gray"),plt.axis("off"),plt.title("corner")


dst = cv2.dilate(dst,None)
img[dst>0.6*dst.max()]=1
plt.figure(),plt.imshow(dst , cmap = "gray"),plt.axis("off"),plt.title("corner")
plt.show()


#shi tomasi detection
img = cv2.imread("sudoku.png",0)
img = np.float32(img)

corners = cv2.goodFeaturesToTrack(img,200,0.01,10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),5,(125,125,125),cv2.FILLED)
    
plt.imshow(img)
plt.show()


print(img.shape)
print(img.size)