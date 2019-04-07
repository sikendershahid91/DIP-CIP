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

    def linear_slice(self, Image , bounds, Gain ) :
        print(type(Image) , Image.dtype)
        print(Image.shape)
        for r in range(0, Image.shape[0] ) :
            for c in range(0, Image.shape[1] ) :
                Image[r, c] = Gain * Image[r, c] \
                              if Image[r,c] >= min(bounds) and \
                                 Image[r,c] <= max(bounds) \
                                 else Image[r,c]

    def constant_slice(self, Image, bounds, Gain ):
        print(bounds) 
        constant = sum(bounds)/2
        print(type(Gain))
        print(type(constant))
        for r in range(0, Image.shape[0] ) :
            for c in range(0, Image.shape[1] ) :
                Image[r,c] = Gain * constant \
                             if Image[r,c] >= min(bounds) and \
                                Image[r,c] <= max(bounds) \
                                else Image[r,c] 

                
    def inverted_linear_slice(self, Image, bounds, Gain): 
        self.linear_slice(Image, [ np.min(Image), min(bounds)  ] , Gain )
        self.linear_slice(Image, [ max(bounds) , np.max(Image) ] , Gain )


    def inverted_constant_slice(self, Image, bounds, Gain):
        self.constant_slice(Image, [ np.min(Image), min(bounds)  ] , Gain )
        self.constant_slice(Image, [ max(bounds) , np.max(Image) ] , Gain )

