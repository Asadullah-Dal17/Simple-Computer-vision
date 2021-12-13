import cv2 as cv 
import os
# images directory path 
dir_path ='../images'

files = os.listdir(dir_path)
not_square = '../Not_squre'
for file in files:
    # creating complete image path 
    img_path = os.path.join(dir_path, file)
    img =cv.imread(img_path)
    height, width = img.shape[:2]
    if height!=width:
        print("not Square")
        ns_path = os.path.join(not_square, file)
        os.rename(img_path, ns_path)
    else:
        print("Square")
    
    # cv.imshow('img', img)
    # cv.waitKey(0)