import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #create background image of height and width
#img[:]= 255,0,0 # add colour in the image
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
#cv2.line(img,(0,0),(100,200),(255,255,0),7)
# first argument img second starting coordinates third height width fourth colour and fifth thickness
# for diagnol line use img.shape points
cv2.rectangle(img,(0,0),(250,300),(0,0,255),3) # same as line
cv2.circle(img,(350,300),30,(255,255,0),3) # same as line but 30 is radius how big small circle
cv2.putText(img,"OpenCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),3) # argument 0.5 define size and 3 thickness

cv2.imshow("Image",img)
cv2.waitKey(0)