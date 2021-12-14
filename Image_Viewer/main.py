import cv2 as cv 
import os
import tkinter as tk
import PIL.Image, PIL.ImageTk
def previous(a):
    print(a)
def Next(a):
    print(a)
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
height=600
width=600
# creating GUI 
root = tk.Tk()
root.title("Image Viewer")
image =loaded_images[0]
# img = loaded_images[0]
# height, width = image.shape[:2]

RGB_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
img_tk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(RGB_img))

canvas = tk.Canvas(root, width = width, height = height)
canvas.pack()
canvas.create_image(50, 50, image=img_tk, anchor=tk.NW)
next_btn = tk.Button(root, text="Next", width=6, height=1, command=lambda: Next('test'))
previous_btn = tk.Button(root, text="Previous", width=6, height=1, command=lambda: previous('test'))
next_btn.pack()
previous_btn.pack()

root.mainloop() 
