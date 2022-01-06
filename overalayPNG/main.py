import cv2 as cv 
import numpy as np

fourground = cv.imread('cheeta.png', cv.IMREAD_UNCHANGED)
back_ground = cv.imread('pexels-francesco-ungaro-2835436.jpg')
cv.imshow('img', back_ground)
fg_h, fg_w = fourground.shape[:2]
x, y = 20, 20
roi = back_ground[y:fg_h+y, x: fg_w+x ]
cv.imshow('roi', roi)
# gettting images channels 
B, G, R, AlPha = cv.split(fourground)
cv.imshow("Alpha", AlPha)
inv_mask = cv.bitwise_not(AlPha)
cv.imshow('inv', inv_mask)
out=cv.bitwise_and(roi, roi,mask=inv_mask)
out2=cv.bitwise_or(fourground,fourground, out,mask=AlPha)

cv.imshow('roi2', out)
cv.imshow('roi3', out2)


cv.imshow('fourground', fourground)
cv.waitKey(0)
