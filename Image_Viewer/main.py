import cv2 as cv 
import os
# loading all the images in directory 
def load_images(dir_path):
    #  getting the list of file in the dir
    files = os.listdir(dir_path)
    for file in files:
        # creating complete image path 
        img_path = os.path.join(dir_path, file)
        img =cv.imread(img_path)
        height, width = img.shape[:2]
        # print(700/height)
        # maintain the ratio if width is greater then height, then resize based on with, otherwise on based on height. 
        if width>height:
            resize_img=cv.resize(img, None, fx=(700/width), fy=(700/width), interpolation=cv.INTER_AREA)
        elif height>width:
            resize_img=cv.resize(img, None, fx=(700/height), fy=(700/height), interpolation=cv.INTER_AREA)
        else:
            resize_img=cv.resize(img, None, fx=(700/width), fy=(700/width), interpolation=cv.INTER_AREA)
        cv.imshow('resize', resize_img)
        cv.waitKey(0)
# images directory path 
dir_path ='../images'
load_images(dir_path)
    # cv.resize()