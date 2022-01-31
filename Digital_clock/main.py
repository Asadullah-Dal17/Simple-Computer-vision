import numpy as np
import cv2 as cv
from datetime import datetime

while True:
    img = np.zeros((100, 210, 3), dtype=np.uint8)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    cv.putText(
        img=img,
        text=f"Time: {current_time}",
        org=(10, 50),
        fontFace=cv.FONT_HERSHEY_PLAIN,
        fontScale=1.5,
        color=(0, 255, 0),
        lineType=cv.LINE_AA,
        thickness=2,
    )

    cv.imshow("frame", img)

    key = cv.waitKey(1)

    if key == ord("q"):
        break
cv.destroyAllWindows()
