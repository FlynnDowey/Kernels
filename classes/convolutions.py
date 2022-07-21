from skimage.exposure import rescale_intensity 
import numpy as np
import argparse
import cv2

class Convolutions:
    def __init__(self, image, K):
        self.image = image
        self.K = K

    def convolve(self):
        (iH, iW) = self.image.shape[:2]
        (kW, kW) = self.K.shape[:2]

        # padding the image so that the output
        # image is the same dimention.
        # p = (f - 1) / 2 ==> n + 2p - f + 1 = n
        pad = (kW - 1) // 2 
        
        # apply the paddig to the image
        image = cv2.copyMakeBorder(self.image, pad, pad, pad, pad,  
            cv2.BORDER_REPLICATE)

        output = np.zeros((iH, iW), dtype="float")

        # slide the kernel across the image (in np arange is indexd by [start, stop))
        for y in np.arange(pad, iH + pad):
            for x in np.arange(pad, iW + pad):
                # get the centre of the pixel
                roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

                # perform the convolution 
                k = (roi * self.K).sum()

                # store the output
                output[y - pad, x - pad] = k
        # rescale the output image
        output = rescale_intensity(output, in_range=(0, 255))
        output = (output * 255).astype("uint8")

        return output

    def getConv(self):
        return self.convolve()