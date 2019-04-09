'''
This script will play a random video on a window
- Press key 'q' to exit
- Press key 'f' to freeze the video
- Press key 'x' to detect edges
'''

import cv2 as cv
import numpy as np

video = cv.VideoCapture('videos/trick.mp4')
if not video:
    raise Exception('Error loading the video')

freeze = False
edges = True

try:
    while video.isOpened():
        if not freeze:
            ret, frame = video.read()
            if not ret:
                video.set(cv.CAP_PROP_POS_FRAMES, 0)
                continue

            frame = cv.resize(frame, dsize=(960, 540), interpolation=cv.INTER_AREA)

            if edges:
                frame = cv.Canny(frame, 20, 150)

            cv.imshow('Trick', frame)


        key = cv.waitKey(25)
        if key == ord('q'):
            break
        elif key == ord('f'):
            freeze = not freeze
        elif key == ord('x'):
            edges = not edges
finally:
    video.release()
    cv.destroyAllWindows()
