import argparse
import numpy as np
import cv2
from classes.convolutions import Convolutions as conv


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
    help="path to image")
args = vars(ap.parse_args())

# common kernels
smallBlur = np.ones((3, 3), dtype="float") * (1.0 / (3 * 3))
largeBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))

# more kernels
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype = "int")

sobelY= np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype = "int")

sobelII= np.array((
    [-10, -2, -1],
    [0, 1, 0],
    [1, 2, 10]), dtype = "int")

# construct the kernel bank
kernelBank = (
    ("small_blur", smallBlur),
    ("large_blur", largeBlur),
    ("sharpen", sharpen),
    ("laplacian", laplacian),
    ("sobel_x", sobelX),
    ("sobel_y", sobelY),
    ("sobel_ii", sobelII))

# read the image & greyscale it
image = cv2.imread(args["image"])
#image = image.reshape(image, (32, 32), cv2.INTER_AREA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray,(500, 500), interpolation=cv2.INTER_AREA)


for (kernelName, K) in kernelBank:
    print("[INFO] applying {} kernel".format(kernelName))
    convOut = conv(gray, K)
    cv2.imshow("Original", gray)
    cv2.imshow("{} - convolve".format(kernelName), convOut.getConv())
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
