import cv2 as cv
import numpy as np
import time 
cap = cv.VideoCapture(0)

frame_counter =0
start_time = time.time()

while True:
    frame_counter +=1
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    key =cv.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv.destroyAllWindows()