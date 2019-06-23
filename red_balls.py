"""
I created this program to find the edges of two red balls in an image
I was able to get around the watermark on the image but not the one at the bottom of the image
One issue is that I think it creates in infinite loop, so when I close the window and try to run again, it won't let me unless I close the console as well
"""

import cv2
import numpy as np

#This method will take in an image and output the canny image to detect edges
def make_canny(image, lower, upper):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, lower, upper)
    return canny

balls = cv2.imread('C:/python_images/red_ball.jpg') #This will find the image in question and store it in the variable
copy_of_balls = np.copy(balls) #This creates a copy of the image so the original is not altered

canny_image = make_canny(copy_of_balls, 200, 250) #This creates a canny image of the copy

#This part adds text to the screen. I was just playing with this
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canny_image,'Hello',(10,100), font, 2,(255,255,255),2,cv2.LINE_AA)

#This displays the image in a window
cv2.imshow('Edges of Balls', canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()