# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:28:07 2020

@author: jrsho
"""


import numpy as np
import time

def reduceToLastNIndices(array, n):
    length = array.size
    if n > length:
        print('Error: The array is not as long as the number specified')
        time.sleep(10)
        return array
    elif n == length:
        print('Error: The array is exactly as long as the number specified. Returning original array')
        time.sleep(10)
        return array
    else:
        newArray = array[(length - n):length]
        return newArray


from picamera import PiCamera

'''
camera = PiCamera()

camera.start_preview()
time.sleep(5)
camera.capture('/home/pi/Desktop/imageFromTestCode.jpg')
camera.stop_preview()
'''

# Testing the camera.capture_sequence() method
# import time
# import picamera
with PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture_sequence([
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        ])
    camera.stop_preview()




