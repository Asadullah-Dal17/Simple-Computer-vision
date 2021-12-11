import cv2
import numpy as np
import pafy # pip3 install youtube-dl

url = "https://youtu.be/p5Z_GGRCI5s"
# video = pafy.new(url)
playlist = pafy.get_playlist(url)
print(playlist)
# best = video.getbest(preftype="mp4")
# captura = cv2.VideoCapture() #Youtube
# captura.open(best.url)

# while True:
#     ret, frame = captura.read()


    
#     cv2.imshow('Salida',frame)
#     k = cv2.waitKey(24)&0xFF
#     if k == 27:
#         break
    
# captura.release()
# cv2.destroyAllWindows()