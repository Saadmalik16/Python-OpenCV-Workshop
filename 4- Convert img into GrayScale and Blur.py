import cv2

img = cv2.imread("img/saad.jpg") #read the image

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #read the image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # kernal 7,7 matrix

cv2.imshow("Saad",img) #show the image
cv2.imshow("Gray Scale",imgGray) #show the image
cv2.imshow("Blur",imgBlur) #show the image
cv2.waitKey(0) #for delay