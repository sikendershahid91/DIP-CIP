#!/usr/bin/env python3

#
# package contains sharpening, smoothing, slicing filters. 
#
# assumptions : dtype - is not floating point
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
                temp_value = gain * image[r, c] \
                              if image[r,c] >= min(bounds) and \
                                 image[r,c] <= max(bounds) \
                                 else image[r, c]
                
                if temp_value > np.iinfo(image.dtype).max:
                    image[r, c] = np.iinfo(image.dtype).max
                elif temp_value < np.iinfo(image.dtype).min:
                    image[r, c] = np.iinfo(image.dtype).min
                else:
                    image[r, c] = temp_value
                    
        return image

    def constant_slice(self, image, bounds, gain):
        print(bounds) 
        constant = sum(bounds)/2
        print(type(gain))
        print(type(constant))
        for r in range(0, image.shape[0] ) :
            for c in range(0, image.shape[1] ) :
                temp_value = gain * constant \
                             if image[r,c] >= min(bounds) and \
                                image[r,c] <= max(bounds) \
                                else image[r,c]
                
                if temp_value > np.iinfo(image.dtype).max:
                    image[r, c] = np.iinfo(image.dtype).max
                elif temp_value < np.iinfo(image.dtype).min:
                    image[r, c] = np.iinfo(image.dtype).min
                else:
                    image[r, c] = temp_value 
                
        return image

    def inverted_linear_slice(self, image, bounds, gain):
        output = self.linear_slice(image, [np.min(image), min(bounds)], gain)
        output = self.linear_slice(output, [max(bounds), np.max(image)], gain)
        return output

    def inverted_constant_slice(self, image, bounds, gain):
        output = self.constant_slice(image, [np.min(image), min(bounds)], gain)
        output = self.constant_slice(output, [max(bounds), np.max(image)], gain)
        return output

