import cv2 

class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        #store images height, width and interpolation
        #methods for resizing 
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, image):
        #resize image (ignore aspect ratio)
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)