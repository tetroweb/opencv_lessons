# text and shapes
import numpy as np
import cv2

#black image
img = np.zeros((500,500,3),np.uint8)
cv2.imshow("black",img)
print("black image shape :",img.shape)

#line
img_line = cv2.line(img,(0,0),(500,500),(0,255,0),3)#(image , start point , end point , color , thickness)
cv2.imshow("line image",img_line)

#rectangle
img_rectangle = cv2.rectangle(img,(0,0),(100,100),(255,0,0),cv2.FILLED)#(image , start point , end point , color , thickness)
cv2.imshow("rectangle ",img_rectangle)

#circle
img_circle = cv2.circle(img , (300,300) ,45 ,(0,0,255),3)#(img , center , radius , color)
cv2.imshow("circle",img_circle)

#text
img_text = cv2.putText(img,"image",(250,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))#(img,start point,font,thickness,color)
cv2.imshow("text",img_text)

cv2.waitKey(0)
cv2.destroyAllWindows()