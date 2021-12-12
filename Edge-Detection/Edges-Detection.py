import cv2 as cv 

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow('img', frame)
    key =cv.waitKey(1)
    if key ==ord('q'):
        break
cv.destroyAllWindows()
cap.release()