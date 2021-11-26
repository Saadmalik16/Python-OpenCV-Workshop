import cv2
import numpy as np

def getContour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_NONE)
    #find contours first perameter image and second is retreval method
    #we have approximation and compressed value and reduce the value and
    #get the contours.
    for cnt in contours:
        area = cv2.contourArea(cnt) # arae of shapes
        print(area)
        if area>500: #size of each shape
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3) # draw the contours
            peri = cv2.arcLength(cnt,True) # get perimaeter and length
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) # get corner points
            print(len(approx))
            objCorner = len(approx) # get corners in the image
            x, y, w, h = cv2.boundingRect(approx)

            if objCorner==3: objType = "Tri"
            elif objCorner==4:
                aspRatio= w/float(h)
                if aspRatio>0.95 and aspRatio<1.05: objType = "Square"
                else: objType = "Rectangle"
            elif objCorner>4: objType = "Circle"
            else: objType = "None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            #put a rectangle on the each image
            cv2.putText(imgContour,objType,(x+(w//2)-10,y+(h//2)-10),
                        cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)
            #text on the image x+(w//h) and next term basically define the
            #place of a text and 0.5 is size and 000 is color and 2 is thickness

img = cv2.imread("img/shapes.png")
imgContour = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)

getContour(imgCanny)


cv2.imshow("Image",img)
cv2.imshow("Image Gray",imgGray)
cv2.imshow("Image Blur",imgBlur)
cv2.imshow("Image Canny",imgCanny)
cv2.imshow("Image Courtour",imgContour)
cv2.imshow("Image Blank",imgBlank)
cv2.waitKey(0)

