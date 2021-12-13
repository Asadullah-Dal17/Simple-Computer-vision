import cv2 as cv 
import os
# images directory path 
dir_path ='../images'

files = os.listdir(dir_path)

for file in files:
    # creating complete image path 
    img_path = os.path.join(dir_path, file)
    img =cv.imread(img_path)
    print(img.shape)
    # cv.imshow('img', img)
    # cv.waitKey(0)