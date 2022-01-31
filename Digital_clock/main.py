import numpy as np
import cv2 as cv

while True:
    img = np.zeros((500, 500, 3), dtype=np.uint8)

    cv.imshow("frame", img)

    key = cv.waitKey(1)

    if key == ord("q"):
        break
cv.destroyAllWindows()
