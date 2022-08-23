import numpy as np
import cv2
import sys
import math

if __name__ == '__main__':
    image = cv2.imread('./Image/IMG_4230.JPG', cv2.IMREAD_ANYCOLOR)
    
    # 顯示原圖
    cv2.imshow('image', image)

    # 圖像旋轉
    rImg = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    rImg2 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    rImg3 = cv2.rotate(image, cv2.ROTATE_180)

    cv2.imshow('rImg_counterclockwise', rImg)
    cv2.imshow('rImg_clockwise', rImg2)
    cv2.imshow('rImg_180', rImg3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()