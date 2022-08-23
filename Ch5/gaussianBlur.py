from pickletools import uint8
import cv2
import numpy as np
import math
from scipy import signal

def getGaussKernel(sigma, H, W):
    gaussMatrix = np.zeros([H, W], np.float32)

    # 得到中心點位置
    cH = (H-1)/2
    cW = (W-1)/2

    # 計算Gauss
    for row in range(H):
        for col in range(W):
            norm2 = math.pow(r-cH, 2) + math.pow(c-cW, 2)
            gaussMatrix[row][col] = math.exp(-norm2/(2*math.pow(sigma, 2)))
    
    # 計算高斯矩陣的和
    sumGM = np.sum(gaussMatrix)
    # 歸一化
    gaussKernel = gaussMatrix/sumGM

    return gaussKernel

def gaussBlur(image, sigma, H, W, _boundary = 'fill', _fillvalue = 0):
    # 構建水平方向上個高斯卷積核心
    gaussKernel_x = cv2.getGaussianKernel(sigma, W, cv2.CV_64F)
    # 轉置
    gaussKernel_x = np.transpose(gaussKernel_x)
    # 圖像矩陣與水平高斯核心卷積
    gaussBlur_x = signal.convolve2d(image, gaussKernel_x, mode = 'same', boundary = _boundary, fillvalue = _fillvalue)
    # 構建垂直方向上個高斯卷積核心
    gaussKernel_y = cv2.getGaussianKernel(sigma, H, cv2.CV_64F)
    # 與垂直方向上的高斯核心旋積核心
    gaussBlur_xy = signal.convolve2d(gaussBlur_x, gaussKernel_y, mode = 'same', boundary = _boundary, fillvalue = _fillvalue)

    return gaussBlur_xy

if __name__ == '__main__':
    image = cv2.imread('../Image/img.jpg')
    cv2.imshow('image', image)

    # 高斯平滑
    blurImage = gaussBlur(image, 5, 51, 51, 'symm')
    # 對blurImage進行灰度級顯示
    blurImage = np.round(blurImage)
    blurImage = blurImage.astype(uint8)
    cv2.imshow('GaussBlur', blurImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()