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

    It also implements the method __iter__. A Camera object can be used as an
    iterator that yields camera frames

    with Camera() as cam:
        for frame in cam:
            cv.imshow(frame)
            cv.waitKey(50)
    '''

    def __init__(self, index=0):
        '''
        Constructor
        :param index: Should be an int number indicating the camera index
        (0 by default)
        '''
        if type(index) != int:
            raise TypeError('Camera index must be a number')
        self.handler = None
        self.index = index

    def init(self):
        '''
        Initializes the camera. Is called automatically when method
        read() is called
        If camera is already initialized, nothing is done
        '''
        if self.handler is None:
            self.handler = cv.VideoCapture(self.index)
            if not self.handler.isOpened():
                raise Exception('Error initializing camera')

    def close(self):
        '''
        Releses the camera. Is called automatically when method
        __exit__ is called. If this method was called previously, this invocation
        doesnt have any effect
        '''
        if not self.handler is None:
            self.handler.release()
            self.handler = None


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tcb):
        self.close()
        return False

    def read(self):
        '''
        Reads the next frame of the camera
        Raises an exception if there was an error
        '''
        if self.handler is None:
            self.init()
        ret, frame = self.handler.read()
        if not ret:
            raise Exception('Error read the next camera frame')
        return frame


    def __iter__(self):
        '''
        Returns an iterator that yields indefinitely camera frames
        '''
        while True:
            frame = self.read()
            yield frame


if __name__ == '__main__':
    # Test
    camera = Camera()
    with camera:
        for frame in camera:
            cv.imshow('Camera', frame)
            cv.waitKey(50)
