import cv2
import numpy as np

img = cv2.imread("img/card.jpg")
width,height = 250,300
pts1 = np.float32([[172,41],[292,67],[141,212],[251,237]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Card",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)