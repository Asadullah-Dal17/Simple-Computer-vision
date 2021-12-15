import cv2 as cv
import numpy as np
import time 
import AiPhile
cap = cv.VideoCapture(0)

frame_counter =0
start_time = time.time()

while True:
    frame_counter +=1
    ret, frame = cap.read()
    if ret is None:
        break
    fps = frame_counter/(time.time() - start_time)
    AiPhile.textBGoutline(frame, f"FPS: {round(fps,2)}", fonts=cv.FONT_HERSHEY_PLAIN, scaling=1.3)
    cv.imshow('frame', frame)
    key =cv.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv.destroyAllWindows()