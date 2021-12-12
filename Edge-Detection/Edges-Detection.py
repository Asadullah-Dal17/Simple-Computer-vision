import cv2 as cv 
import time 
cap = cv.VideoCapture(0)
start_time = time.time()
frame_counter =0
while True:
    frame_counter +=1
    ret, frame = cap.read()
    fps = frame_counter/(time.time() - start_time)
    print(fps)
    cv.imshow('img', frame)
    key =cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()