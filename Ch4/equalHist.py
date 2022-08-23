import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

def calcGrayHist(image):
    rows, cols = image.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    
    for i in range(rows):
        for j in range(cols):
            grayHist[[image[i][j]]] += 1
    
    return grayHist

def equalHist(image):
    rows, cols = image.shape[:2]
    # 計算灰度直方圖
    equalHist = calcGrayHist(image)
    # 計算累加灰度直方圖
    zeroCumuMoment = np.zeros([256], np.uint64)
    for p in range(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p-1] + grayHist[p]
    # 根據累加灰度直方圖得到輸入灰度級和輸出灰度級之間的映射關係
    outPut_q = np.zeros([256], np.uint8)
    coefficient = 256.0 / (rows * cols)
    for p in range(256):
        q = coefficient * float(zeroCumuMoment[p]) - 1
        if q >= 0:
            outPut_q[p] = math.floor(q)
        else:
            outPut_q[p] = 0
    # 得到直方圖均衡化的影像
    equalHistImage = np.zeros(image.shape, np.uint8)
    for i in range(rows):
        for j in range(cols):
            equalHistImage[i][j] = outPut_q[image[i][j]]
    
    return equalHistImage

if __name__ == "__main__":
    image = cv2.imread("../Image/img.jpg")
    # 計算灰度直方圖
    grayHist = calcGrayHist(image)
    equalHistImage = equalHist(image)

    cv2.imshow("I", image)
    cv2.imshow("equalHistImage", equalHistImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()