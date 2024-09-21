import numpy as np
import cv2
import imutils
import datetime

gun_cascade = cv2.CascadeClassifier("D:\python projects\gundetect\cascade.xml")
camera = cv2.VideoCapture(0)
firstframe = None
gun_exist = None

while True:
    ret, frame = camera.read() # HERE RET IS A BOOL VARIABLE THAT RETURNS TRUE IF THE CAMERA IS CAPTURING 
                               # AND FALSE IF IT IS NOT CAPTURIG
                               # FRAME HERE CONTAINS THE IMAGE THAT IS CAPTURED AS A NUMPY ARRAY
    
    frame = imutils.resize(frame, width = 500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100,100))

    if len(gun) > 0:
        gun_exist = True
    
    for (x,y,w,h) in gun:
        frame = cv2.rectangle(frame, (x,y), ((x+w),(y+h)), (255,0,0), 2) # HERE X,Y ARE THE COORDINATES
                                                                         # OF THE TOP LEFT CORNER 
                                                                         # OF THE RECTANGLE
                                                                         # AND (x+w),(y+h) THIS IS THE WAY
                                                                         # TO CALCULATE THE BOTTOM RIGHT 
                                                                         # CORNER OF THE RECTANGLE
        
        roi_gray = gray[y : y+h, x : x+w] # THIS IS A WAY OF SLICING AND EXTRACTING CERTAIN AREA OF THE IMAGE
        roi_frame = frame[y : y+h, x : x+w]
    
    if firstframe is None:
        firstframe = gray
        continue

    cv2.imshow("security feed", frame)
    key = cv2.waitKey(1) & 0xFF # cv2.waitKey(1): This command pauses the program for 1 millisecond, 
                                # waiting to see if any key is pressed. 
                                # If no key is pressed, it moves on, 
                                # but if a key is pressed, it captures that key's code.
                                # & 0xFF: This part helps make sure the keycode is clean and simple, 
                                # taking only the important part (the last 8 bits) of the key press. 
                                # This makes it easier to compare with specific keys, 
                                # like checking if 'q' was pressed.
    if key == ord('q'):
        break

if gun_exist:
    print("guns detected")

else:
    print("no gun detected")

camera.release()
cv2.destroyAllWindows()