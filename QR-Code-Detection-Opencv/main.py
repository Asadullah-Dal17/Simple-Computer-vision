import cv2 as cv
import numpy as np
import time 
import AiPhile
cap = cv.VideoCapture(0)

frame_counter =0
start_time = time.time()
QR_Decoder = cv.QRCodeDetector()
while True:
    frame_counter +=1
    ret, frame = cap.read()
    if ret is None:
        break
    data, bbox, rectified_img = QR_Decoder.detectAndDecode(frame)
    if bbox is not None:
        box =bbox.astype(int)
        cv.circle(frame, box[0][0], 5, AiPhile.INDIGO, -1)
        frame=AiPhile.fillPolyTrans(frame, box, AiPhile.GREEN, 0.5)
        AiPhile.textBGoutline(frame, f"data: {data}",position=  box[0][0],fonts=cv.FONT_HERSHEY_PLAIN, scaling=0.9)

        # cv.waitKey(0)
    fps = frame_counter/(time.time() - start_time)

    AiPhile.textBGoutline(frame, f"FPS: {round(fps,2)}", fonts=cv.FONT_HERSHEY_PLAIN, scaling=1.3)
       
    cv.imshow('frame', frame)
    key =cv.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv.destroyAllWindows()