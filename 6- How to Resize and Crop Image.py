import cv2
import numpy

img = cv2.imread("img/saad.jpg")
print(img.shape) #first argument height secnd width and third show coloured
imgResize = cv2.resize(img,(300,250)) #first argument width second height
imgCropped = img[0:100,80:120] #first argument height second width

cv2.imshow("Saad",img)
cv2.imshow("Reszie Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)