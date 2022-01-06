import cv2 as cv 
import numpy as np

fourground = cv.imread('cheeta.png', cv.IMREAD_UNCHANGED)
back_ground = cv.imread('pexels-francesco-ungaro-2835436.jpg')

# gettting images channels 
B, G, R, AlPha = cv.split(fourground)
cv.imshow("Alpha", AlPha)
cv.imshow('fourground', fourground)
cv.waitKey(0)
