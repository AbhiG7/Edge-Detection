import cv2

'''
I used a stock video and created a program that detects the edges in the video
One issue with this is that if the whole video is left to play, the window crashes and says it's not responding
'''

#This method will take in an image and output the canny image to detect edges
def make_canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    canny = cv2.Canny(blur, 50, 100)
    return canny

cap = cv2.VideoCapture('C:/python_images/test2.mp4') #This will start the video capture

#This loop will loop through each frame of the video, creating a canny image of each frame and displaying it
while (cap.isOpened()):
    _, frame = cap.read() #This will take each frame if the video, I assume
    canny_frame = make_canny(frame)
    
    #This part adds text to the screen. I was just playing with this
    font = cv2.FONT_ITALIC
    cv2.putText(canny_frame,'Insert Coordinates Here',(10,100), font, 2,(255,255,255),2,cv2.LINE_AA)
    
    cv2.imshow("Video", canny_frame)
    
    #This statement will allow you to close the video if q is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()