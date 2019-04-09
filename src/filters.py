#!/usr/bin/env python3

#
# package contains sharpening, smoothing, slicing filters. 
#

import numpy as np 
import cv2

class Sharpen:
    def __init__(self):
        pass

class Smooth:
    def __init__(self):
        pass

class Slice:
    def __init__(self):
        print('starting slicing')
        pass

    def linear_slice(self, image, bounds, gain):
        print(type(image), image.dtype, image.shape)
        print("Slicing Range: ", bounds, "Gain = ", gain)

        for r in range(0, image.shape[0]):
            for c in range(0, image.shape[1]):
                image[r, c] = gain * image[r, c] \
                              if image[r,c] >= min(bounds) and \
                                 image[r,c] <= max(bounds) \
                                 else image[r, c]

        return image

    def constant_slice(self, image, bounds, gain):
        print(bounds) 
        constant = sum(bounds)/2
        print(type(gain))
        print(type(constant))
        for r in range(0, image.shape[0] ) :
            for c in range(0, image.shape[1] ) :
                image[r,c] = gain * constant \
                             if image[r,c] >= min(bounds) and \
                                image[r,c] <= max(bounds) \
                                else image[r,c]
        return image

    def inverted_linear_slice(self, image, bounds, gain):
        output = self.linear_slice(image, [np.min(image), min(bounds)], gain)
        output = self.linear_slice(output, [max(bounds), np.max(image)], gain)
        return output

    def inverted_constant_slice(self, image, bounds, gain):
        output = self.constant_slice(image, [np.min(image), min(bounds)], gain)
        output = self.constant_slice(output, [max(bounds), np.max(image)], gain)
        return output

