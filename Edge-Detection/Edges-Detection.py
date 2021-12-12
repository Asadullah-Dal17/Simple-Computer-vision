import cv2 as cv 
import time 
cap = cv.VideoCapture(0)
start_time = time.time()
frame_counter =0
while True:
    frame_counter +=1
    ret, frame = cap.read()
    # applying Gaussian Blur to Remove the Noise and preserving the Edges 
    denoise_frame = cv.GaussianBlur(frame, (3,3), 0)

    edges_frame = cv.Canny(denoise_frame, 100,200)
    cv.imshow('Edges', edges_frame)
    fps = frame_counter/(time.time() - start_time)
    # print(fps)

    cv.putText(frame, f'FPS: {round(fps, 2)}', (40,30), cv.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
    
    cv.imshow('img', frame)
    key =cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()