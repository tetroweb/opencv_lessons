#image blur(detay azalır , gürültü engeller)
import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# #
# img = cv2.imread("img.png")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# plt.figure()
# plt.imshow(img , cmap = "gray")
# plt.axis("off")


# #mean blur - ortalama bulanıklaştırma - kernel size kadar pixel alınır ve ortalaması ortadaki pixel değere atanır - 

# dst2 = cv2.blur(img , ksize=(3,3))
# plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("Mean - Ortalama")


# #gaussian blur

# gb = cv2.GaussianBlur(img , ksize=(3,3) , sigmaX = 7)
# plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gaussian blur")



# #median blur - medyan blur

# mb = cv2.medianBlur(img , ksize=3)
# plt.figure(),plt.imshow(mb),plt.axis("off"),plt.title("Median blur")


# #noise - gürültü ekleme

# def gaussianNoise(image):
#     row , col , ch = image.shape
#     mean = 0
#     var = 0.05
#     sigma = var**0.5
    
#     gauss = np.random.normal(mean,sigma,(row,col,ch))
#     gauss = gauss.reshape(row,col,ch)
#     noisy = image + gauss
    
#     return noisy


# #make normalize
# img = cv2.imread("img.png")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# gaussianNoisyImage = gaussianNoise(img)
# plt.figure()
# plt.imshow(gaussianNoisyImage, cmap="gray" )
# plt.axis("off")
# plt.show()


#salt-pepper noise 

def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    
    # Salt (tuz) eklemek için
    num_salt = np.ceil(amount * image.size * s_vs_p).astype(int)
    coords1 = [np.random.randint(0, i, num_salt) for i in image.shape]
    noisy[tuple(coords1)] = 1
    
    # Pepper (biber) eklemek için
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p)).astype(int)
    coords2 = [np.random.randint(0, i, num_pepper) for i in image.shape]
    noisy[tuple(coords2)] = 0
    
    return noisy

img = cv2.imread("img.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

sp_image = saltPepperNoise(img)
plt.figure(),plt.imshow(sp_image),plt.axis("off"),plt.title("sp_image")
plt.show()



#coords içinde oluşturduğumuz koordinatların düzgün şekilde çalışması için tuple içine almamız gerekiyor