import numpy as np
import matplotlib.pyplot as plt
import cv2

import warnings
warnings.filterwarnings("ignore")

matris = np.array([
    [[200,200,200],[100,100,100]],
    [[150,150,150],[100,100,100]],
    [[170,170,170],[80,80,80]],
    [[150,150,150],[30,30,30]]
])

print(matris[(1,1,1)])


img = cv2.imread("img.png")
copy = np.copy(img)
num_salt = np.ceil(0.004 * img.size * 0.5).astype(int)

coords = [np.random.randint(0,i-1,num_salt) for i in img.shape ]# num_salt kadar satır sutun ve index ataması yapar 28800 tane beyaz ve siyah pixel oluşur
#resmin boyutu 1440000  siyah ve beyaz pixel sayısı 28800  amount (0.004) sayısını arttırıp azaltarak toplam siyah-beyaz pixel sayısıyla oynayabiliriz ve bunların oranlarını ise s_vs_p(0.5) ile değiştirebiliriz

print(img.size)



# list1 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
#                   [[11,12,13],[14,15,16],[17,18,19]],
#                   [[21,22,23],[24,25,26],[27,28,29]]])
# list2 = [np.random.randint(0,i,int(list1.size)) for i in list1.shape]


# print(list2[0])
# print("--------------------------------------------")
# print(list2[1])
# print("--------------------------------------------")
# print(list2[2])
# print("--------------------------------------------")
# print(list1[tuple(list2)])






