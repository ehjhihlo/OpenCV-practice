import cv2
import numpy as np
import matplotlib.pyplot as plt

def calcGrayHist(image):
    rows, cols = image.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    
    for i in range(rows):
        for j in range(cols):
            grayHist[[image[i][j]]] += 1
    
    return grayHist

if __name__ == "__main__":
    image = cv2.imread("../Image/img.jpg")
    # 計算灰度直方圖
    grayHist = calcGrayHist(image)

    plt.plot(range(256), grayHist, 'r', linewidth = 2, c = 'black')
    # 設定坐標軸範圍
    y_maxValue = np.max(grayHist)
    plt.axis([0, 255, 0, y_maxValue])
    # 設定坐標軸標籤
    plt.xlabel('Gray Level')
    plt.ylabel('Number of Pixels')

    plt.show()