# import image 
import cv2

img = cv2.imread("img.png",0)

cv2.imshow("demo",img)

k = cv2.waitKey(0) &0XFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    print("Fuck you") 