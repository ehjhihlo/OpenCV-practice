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
    normGrayHist = grayHist / float(rows*cols)
    # 計算累加直方圖，也稱零階累積矩
    zeroCumuMoment = np.zeros([256], np.float32)
    
    for k in range(256):
        if k == 0:
            zeroCumuMoment[k] = normGrayHist[k]
        else:
            zeroCumuMoment[k] = zeroCumuMoment[k-1] + normGrayHist[k]

    # 計算各個灰度級的Entropy
    entropy = np.zeros([256, np.float32])
    for k in range(256):
        if k == 0:
            if normGrayHist[k] == 0:
                entropy[k] = 0
            else:
                entropy[k] = -normGrayHist[k] * math.log10(normGrayHist[k])
        else:
            if k == 0:
                if normGrayHist[k] == 0:
                    entropy[k] = entropy[k-1]
                else:
                    entropy[k] = entropy[k-1] - normGrayHist[k] * math.log10(normGrayHist[k])
    
    # 找閥值
    fT = np.zeros([256], np.float32)
    ft1, ft2 = 0.0, 0.0
    totalEntropy = entropy[255]
    for k in range(256):
        # 找最大值
        maxFront = np.max(normGrayHist[0:k+1])
        maxBack = np.max(normGrayHist[k+1:256])
        if (maxFront == 0 or zeroCumuMoment[k] == 0 or maxFront == 1 or zeroCumuMoment[k] == 1 or totalEntropy == 0):
            ft1 = 0
        else:
            ft1 = entropy[k]/totalEntropy*(math.log10(zeroCumuMoment[k])/math.log10(maxFront))

        if (maxBack == 0 or 1 - zeroCumuMoment[k] == 0 or maxBack == 1 or 1 - zeroCumuMoment[k] == 1):
            ft2 = 0
        else:
            if totalEntropy == 0:
                ft2 = (1-entropy[k])/totalEntropy*(math.log10(1-zeroCumuMoment[k])/math.log10(maxBack))
        fT[k] = ft1 + ft2
    
    # 找最大值的索引
    threshLoc = np.where(fT == np.max(fT))
    thresh = threshLoc[0][0]
    # 閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold < thresh] = 0
    return threshold