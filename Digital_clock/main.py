import numpy as np
import cv2 as cv
from datetime import datetime

while True:
    img = np.zeros((500, 500, 3), dtype=np.uint8)

    now = datetime.now()
    current_time = now.strftime("%H %M %S")
    print(current_time)

    cv.imshow("frame", img)

    key = cv.waitKey(1)

    if key == ord("q"):
        break
cv.destroyAllWindows()
