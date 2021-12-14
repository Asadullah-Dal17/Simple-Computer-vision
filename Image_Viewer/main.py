import cv2 as cv 
import os
import tkinter as tk
import PIL.Image, PIL.ImageTk
counter_1 =0
def previous(img_list):
    global counter_1
    counter_1 -=1
    # print(counter_1)
    if counter_1 <0:
        counter_1 =0
    image = img_list[counter_1]
    img_tk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(image))
    panel.config(image=img_tk)
    panel.image = img_tk
    # print('previous button pressed ')

def Next(img_list):
    global counter_1
    counter_1 +=1
    # print(counter_1)
    if counter_1 >=len(img_list):
        counter_1 =0
    image = img_list[counter_1]
    img_tk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(image))
    panel.config(image=img_tk)
    panel.image = img_tk
    # RGB_img = cv.cvtColor(img_list[0], cv.COLOR_BGR2RGB)
    # img_tk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(RGB_img))
    # root.config(image=img_tk)
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
        RGB_img = cv.cvtColor(resize_img, cv.COLOR_BGR2RGB)
        
        loaded_image.append(RGB_img)
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
# creating new windown with in window 
RGB_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)
img_tk = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(RGB_img))
#divide window into two sections. One for image. One for buttons

top = tk.Frame(root)
top.pack(side="top")
bottom = tk.Frame(root)
bottom.pack(side="bottom")
panel = tk.Label(root, image = img_tk)
panel.image = img_tk # keep a reference!
panel.pack(side = "top", fill = "both", expand = "yes")


# canvas = tk.Canvas(root, width = width, height = height)
# canvas.pack()
# canvas.create_image(50, 50, image=img_tk, anchor=tk.NW)
next_btn = tk.Button(root, text="Next", width=10, height=2, command=lambda: Next(loaded_images))
previous_btn = tk.Button(root, text="Previous", width=10, height=2, command=lambda: previous( loaded_images))

next_btn.pack(side="right",padx=30)
previous_btn.pack(side="left", padx=30)
root.mainloop() 
