import cv2

webcam = cv2.VideoCapture(0) # by default 0 is for default camera
webcam.set(3,640) # 3 is set for width
webcam.set(4,480) # 4 is set for height
webcam.set(10,100) # 10 is set for brightness

while True:
    success, img = webcam.read() # success is boolean variable and all the image come from vedio = img
    cv2.imshow("LiveCam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # wait key for delay and 0xFF for close the vedio
        break