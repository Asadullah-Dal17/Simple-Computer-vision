import cv2 as cv 
import os
import tkinter as tk
import PIL.Image, PIL.ImageTk

# loading all the images in directory 
def load_images(dir_path):
    #  getting the list of file in the dir
    files = os.listdir(dir_path)
    loaded_image = []
    value = 500
    for file in files:
        # creating complete image path 
        img_path = os.path.join(dir_path, file)
        img =cv.imread(img_path)
        height, width = img.shape[:2]
        # print(value/height)
        # maintain the ratio if width is greater then height, then resize based on with, otherwise on based on height. 
        if width>height:
            resize_img=cv.resize(img, None, fx=(value/width), fy=(value/width), interpolation=cv.INTER_AREA)
        elif height>width:
            resize_img=cv.resize(img, None, fx=(value/height), fy=(value/height), interpolation=cv.INTER_AREA)
        else:
            resize_img=cv.resize(img, None, fx=(value/width), fy=(value/width), interpolation=cv.INTER_AREA)
        # cv.imshow('resize', resize_img)
        # cv.waitKey(0)
        loaded_image.append(resize_img)
    print('loaded all files .')
    
    return loaded_image
dir_path = '../images'
loaded_images =load_images(dir_path)
img = loaded_images[0]
height, width = img.shape[:2]
RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# creating GUI 
root = tk.Tk()
root.title("Image Viewer")

img_tk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(RGB_img))

canvas = tk.Canvas(root, width = width, height = height)
canvas.pack()
canvas.create_image(0, 0, image=img_tk, anchor=tk.NW)
root.mainloop() 
