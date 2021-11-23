import cv2

vedio = cv2.VideoCapture("video/car.mp4") #for add video

while True:
    success, img = vedio.read() # success is boolean variable and all the image come from vedio = img
    cv2.imshow("Car",img)
    if cv2.waitKey(10) & 0xFF == ord('q'): # wait key for delay and 0xFF for close the vedio
        break
