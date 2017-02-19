import numpy as np
import cv2
import os
import time
cap = cv2.VideoCapture("movie.mp4")
directory='video'
index=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame',frame)
        #cv2.waitKey(300)
        #time.sleep(1)
        #cv2.imwrite(str('/video/frame'+str(index))+".jpg",frame)
        filename="video/frame"+str(index)+".jpg"
        #print(filename)
        #cv2.imwrite(filename,frame)
        index+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()