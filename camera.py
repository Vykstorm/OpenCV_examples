'''
This script captures your camera image and display it on a window
- Press q to exit the program
- Press f to freeze/unfreeze the camera
- Press z to change image mode: blur / edge detector / binary thresholding
'''

import cv2 as cv
import numpy as np
from math import floor


cam = cv.VideoCapture(0)
if not cam.isOpened():
    raise Exception('Camera couldnt be opened')

fps = 15
freeze = False
mode = 0

try:
    while True:
        # Capture the next frame
        if not freeze:
            ret, frame = cam.read()
            if not ret:
                raise Exception('Failed getting camera image')

            if mode == 0:
                frame = cv.medianBlur(frame, 15)
            elif mode == 1:
                frame = cv.Canny(frame, 50, 150)
            elif mode == 2:
                frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                frame = cv.adaptiveThreshold(frame, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 17, 3)

            cv.imshow('Camera', frame)

        key = cv.waitKey(floor((1.0 / fps) * 1000))

        if key == ord('q'):
            break
        elif key == ord('f'):
            freeze = not freeze
        elif key == ord('z'):
            mode = (mode + 1) % 3

finally:
    cam.release()
    cv.destroyAllWindows()
