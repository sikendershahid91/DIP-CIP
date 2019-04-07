#!/usr/bin/env python3

import sys
sys.path.insert(0,'src/')

from filters import Slice

import numpy as np
import cv2

if __name__ == '__main__':
## TESTS 
   
    aImage = np.array([
        [1, 2, 3],
        [3, 2, 1],
        [3, 4, 2]] )
    
    Slice().linear_slice( aImage , [2, 3], 3 ) 
    print(aImage)
    Slice().inverted_linear_slice( aImage, [3, 5], 0.5 )
    print(aImage)
    
    aImage = np.array([
        [1, 2, 3],
        [3, 2, 1],
        [3, 4, 2]] )
    Slice().constant_slice( aImage, [ 2, 3], 3)
    print(aImage)
    Slice().inverted_constant_slice( aImage, [3 , 5 ], 0.5 )
    print(aImage) 

    aImage = np.array([
        [1, 2, 3],
        [3, 2, 1],
        [3, 4, 2]])

    import  matplotlib.pyplot as plt
    input_image = cv2.imread("images/Lenna.png", 0)
    
    while True:
        print( np.min(input_image), np.max(input_image) )
        plt.imshow(input_image)
        plt.show()
        gain = input('what gain: ' )
        a, b = input('what bounds ' ).split() 
        Slice().constant_slice( input_image, [float(a) , float(b)], float(gain) )
        plt.imshow(input_image)
        plt.show()
        cv2.waitKey(0) 

