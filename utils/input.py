
import cv2 as cv

def waitKey(t=-1):
    '''
    This method is the same as OpenCV waitKey() method, but it returns
    a char object instead of an integer
    '''
    return chr(cv.waitKey(t) & 255)
