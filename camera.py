'''
This script captures your camera image and display it on a window
Press q to exit the program
Press f to freeze/unfreeze the camera
Press z to blur the image
'''

import cv2 as cv
import numpy as np
from math import floor


cam = cv.VideoCapture(0)
if not cam.isOpened():
    raise Exception('Camera couldnt be opened')

fps = 15
freeze = False
blur = False
edges = False

try:
    while True:
        # Capture the next frame
        if not freeze:
            ret, frame = cam.read()
            if not ret:
                raise Exception('Failed getting camera image')

            if blur:
                frame = cv.medianBlur(frame, 15)
            if edges:
                frame = cv.Canny(frame, 50, 150)

            cv.imshow('Camera', frame)

        key = cv.waitKey(floor((1.0 / fps) * 1000))

        if key == ord('q'):
            break
        elif key == ord('f'):
            freeze = not freeze
        elif key == ord('z'):
            blur = not blur
        elif key == ord('x'):
            edges = not edges

finally:
    cam.release()
    cv.destroyAllWindows()
