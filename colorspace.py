'''
Script that shows how to switch between different color spaces
It will convert the camera input image to an HSV color space to track an object with blue
color

This example follows the tutorial on this web page:
https://docs.opencv.org/trunk/df/d9d/tutorial_py_colorspaces.html
'''


import cv2 as cv
import numpy as np
from math import floor


# The next lines of code prints on stdout all the possible values to be passed to the
# flag parameter on the function cvtColor() to switch between image color spaces

print('Switch color spaces flags:')
methods = [key for key in dir(cv) if key.startswith('COLOR_')]

cols = 4
rows = len(methods) // cols
if rows * cols < len(methods):
    rows += 1

for i in range(0, rows):
    print('  '.join([method.rjust(30) for method in methods[i*cols:min((i+1)*cols, len(methods))]]) )
print()


cam = cv.VideoCapture(0)
if not cam.isOpened():
    raise Exception('Camera couldnt be opened')


fps = 10

try:
    while True:
        # Capture the next frame
        ret, frame = cam.read()
        if not ret:
            raise Exception('Failed getting camera image')

        # Switch color space to HSV
        frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Define HSV range to track the object
        lower_bound = np.array([110,50,50])
        upper_bound = np.array([130,255,255])

        # Apply a treshold on the image using the range defined
        mask = cv.inRange(frame, lower_bound, upper_bound)

        # Merge the original image with the mask using
        frame = cv.bitwise_and(frame, frame, mask)

        # Show the image
        cv.imshow('Camera', frame)

        key = cv.waitKey(floor((1.0 / fps) * 1000))

        if key == ord('q'):
            break

finally:
    cam.release()
    cv.destroyAllWindows()
