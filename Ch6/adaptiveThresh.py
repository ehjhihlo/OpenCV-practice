import cv2
import numpy as np

def adaptiveThresh(I, winsize, ratio=0.15):
    I_mean = cv2.boxFilter(I, cv2.CV_32FC1, winsize)
    out = I - (1.0-ratio)*I_mean
    out[out>=0] = 255
    out[out<0] = 0
    out = out.astype(np.uint8)
    return out