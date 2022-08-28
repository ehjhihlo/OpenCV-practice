import numpy as np
import math

def calcGrayHist(image):
    rows, cols = image.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    
    for i in range(rows):
        for j in range(cols):
            grayHist[[image[i][j]]] += 1
    
    return grayHist

def threshEntropy(image):
    rows, cols = image.shape
    # 計算灰度直方圖
    grayHist = calcGrayHist(image)
    # 歸一化
    uniformGrayHist = grayHist / float(rows*cols)
    # 計算零階累積矩與一階累積矩
    zeroCumuMoment = np.zeros([256], np.float32)
    oneCumuMoment = np.zeros([256], np.float32)
    
    for k in range(256):
        if k == 0:
            zeroCumuMoment[k] = uniformGrayHist[0]
            oneCumuMoment[k] = k*uniformGrayHist[0]
        else:
            zeroCumuMoment[k] = zeroCumuMoment[k-1] + uniformGrayHist[k]
            oneCumuMoment[k] = oneCumuMoment[k-1] + k*uniformGrayHist[k]
    # 計算類別方差
    variance = np.zeros([256], np.float32)
    for k in range(256):
        if zeroCumuMoment[k] == 0 or zeroCumuMoment[k] == 1:
            variance[k] = 0
        else:
            variance[k] = math.pow(oneCumuMoment[255]*zeroCumuMoment[k]-oneCumuMoment[k], 2) / (zeroCumuMoment[k]*(1.0-zeroCumuMoment[k]))

    # 找最大值的索引
    threshLoc = np.where(variance[0:255] == np.max(variance[0:255]))
    thresh = threshLoc[0][0]
    # 閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold < thresh] = 0
    return threshold