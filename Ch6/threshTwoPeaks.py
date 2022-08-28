import numpy as np

def calcGrayHist(image):
    rows, cols = image.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    
    for i in range(rows):
        for j in range(cols):
            grayHist[[image[i][j]]] += 1
    
    return grayHist

def threshTwoPeaks(image):
    # 計算灰度直方圖
    histogram = calcGrayHist(image)
    # 找到灰度直方圖的最大峰值對應的灰度值
    maxLoc = np.where(histogram == np.max(histogram))
    firstPeak = maxLoc[0][0]
    # 尋找灰度直方圖的第二個峰值對應的灰度值
    measureDists = np.zeros([256], np.float32)

    for k in range(256):
        measureDists[k] = pow(k-firstPeak, 2) * histogram[k]
    
    maxLoc2 = np.where(measureDists == np.max(measureDists))
    secondPeak = maxLoc2[0][0]
    # 找到兩個峰值之間最小值對應的灰度值，作為閥值
    thresh = 0
    if firstPeak > secondPeak: # 第一個峰值在第二個峰值右側
        temp = histogram[int(secondPeak):int(firstPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = secondPeak + minLoc[0][0] + 1
    else: # 第一個峰值在第二個峰值左側
        temp = histogram[int(firstPeak):int(secondPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = firstPeak + minLoc[0][0] + 1
    # 閥值處理
    threshImage_out = image.copy()
    threshImage_out[threshImage_out > thresh] = 255
    threshImage_out[threshImage_out < thresh] = 0

    return (thresh, threshImage_out)   