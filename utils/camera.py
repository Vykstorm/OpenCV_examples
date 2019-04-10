
import cv2 as cv


class Camera:
    '''
    This is a helper class to capture the camera image using OpenCV
    It defines the context manager protocol (__enter__ and __exit__) methods, so
    you can write a program like this:

    with Camera() as cam:
        frame = cam.read()
        cv.imshow(frame)
        cv.waitKey(50)
    '''

    def __init__(self, index=0):
        if type(index) != int:
            raise TypeError('Camera index must be an integer')
        self.handler = None
        self.index = index

    def init(self):
        if self.handler is None:
            self.handler = cv.VideoCapture(self.index)
            if not self.handler.isOpened():
                raise Exception('Error initializing camera')

    def close(self):
        if not self.handler is None:
            self.handler.release()
            self.handler = None


    def __enter__(self):
        self.init()
        return self

    def __exit__(self, exc_type, exc_value, tcb):
        self.close()
        return False

    def read(self):
        ret, frame = self.handler.read()
        if not ret:
            raise Exception('Error read the next camera frame')
        return frame


if __name__ == '__main__':
    # Test
    cam = Camera()
    cam.init()
    with cam as camera:
        while True:
            frame = camera.read()
            cv.imshow('Camera', frame)
            cv.waitKey(50)
