import cv2
import numpy as np

img = cv2.imread("img/saad.jpg") #read the image
kernal = np.ones((5,5),np.uint8) #unsinged integer 8 and 5,5 is size of kernal

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #read the image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # kernal 7,7 matrix
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernal,iterations=1) # iteration define the thickness
imgEroded = cv2.erode(imgDialation,kernal,iterations=1) # iteration define the thickness


cv2.imshow("Saad",img) #show the image
cv2.imshow("Gray Scale",imgGray) #show the image
cv2.imshow("Blur",imgBlur) #show the image
cv2.imshow("Canny",imgCanny) #show the image
cv2.imshow("Dilate",imgDialation) #show the image
cv2.imshow("Eroded",imgEroded) #show the image
cv2.waitKey(0) #for delay