'''
This script is a simple test for opencv. It should work fine if you installed
the library correctly on your system

It creates a tv random noise effect
Also it will print the opencv library version
'''

from time import time
from numpy import uint8
from numpy.random import rand
import cv2



xy=(512,512)
Nf = 500

def noisytv():
    imgs = (rand(Nf,xy[0],xy[1])*255).astype(uint8)
    while True:
        for i in imgs:
            cv2.imshow('test',i)
            cv2.waitKey(3) #integer milliseconds, 0 makes wait forever

# Print opencv version
print('OpenCV version: ', cv2.__version__.rjust(7))

noisytv()
