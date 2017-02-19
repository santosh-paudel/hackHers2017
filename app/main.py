# import numpy as np
# import cv2

# cap = cv2.VideoCapture('movie.mp4')
# directory='video'
# index=0;
# while(cap.isOpened()):
#     ret, frame = cap.read()

#     #gray = cv2.cvtColor(frame)
#     cv2.imwrite(str('/video/frame'+str(1)),frame)

#     #cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# '''
# Simply display the contents of the webcam with optional mirroring using OpenCV 
# via the new Pythonic cv2 interface.  Press <esc> to quit.
# '''

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

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #cv2.imwrite('Tas.jpg',frame)
        #os.system("python3 image_data.py < Tas.jpg")
        cv2.imshow('frame',frame)
        #cv2.waitKey(300)
        #time.sleep(1)
        #cv2.imwrite(str('/video/frame'+str(index))+".jpg",frame)
        filename="video/frame"+str(index)+".jpg"
        print(filename)
        cv2.imwrite(filename,frame)
        index+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
