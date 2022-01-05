import cv2

faceCascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")
img = cv2.imread("img/saad.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y), ## Origion point starting
                  (x+w,y+h), ## corner points
                  (255,0,0),2) ## color and thickness

cv2.imshow("Image",img)
cv2.waitKey(0)