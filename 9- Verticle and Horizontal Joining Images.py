import cv2
import numpy as np

img = cv2.imread("img/saad.jpg")
img2 = cv2.imread("img/lambo.png")

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow("Horizantal",imgHor)
cv2.imshow("Verticle",imgVer)
cv2.waitKey(0)