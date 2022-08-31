import numpy as np
import cv2
from scipy import signal

def roberts(I, _boundary = 'fill', _fillValue = 0):
    # 影像寬高
    H1, W1 = I.shape[0:2]
    # 核心寬高
    H2, W2 = 2, 2
    # 卷積核心
    R1 = np.array([[1, 0], [0, -1]], np.float32)
    # 錨點位置
    kr1, kc1 = 0, 0
    # 計算卷積
    IconR1 = signal.convolve2d(I, R1, mode = 'full', boundary = _boundary, fillvalue = _fillValue)
    IconR1 = IconR1[H2-kr1-1:H1+H2-kr1-1, W2-kc1-1:W1+W2-kc1-1]
    # 卷積核心
    R2 = np.array([[1, 0], [-1, 0]], np.float32)
    IconR2 = signal.convolve2d(I, R2, mode = 'full', boundary = _boundary, fillvalue = _fillValue)
    # 錨點位置
    kr2, kc2 = 0, 1
    # 根據錨點的位置擷取full卷積，從而得到same卷積
    IconR2 = IconR2[H2-kr2-1:H1+H2-kr2-1, W2-kc2-1:W1+W2-kc2-1]

    return (IconR1, IconR2)

if __name__ == '__main__':
    image = cv2.imread('../Image/img.jpg', cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', image)

    IconR1, IconR2 = roberts(image, 'symm')
    # 45度方向上的邊緣強度灰度級顯示
    IconR1 = np.abs(IconR1)
    edge_45 = IconR1.astype(np.uint8)
    cv2.imshow('edge_45', edge_45)
    # 135度方向上的邊緣強度灰度級顯示
    IconR2 = np.abs(IconR2)
    edge_135 = IconR2.astype(np.uint8)
    cv2.imshow('edge_135', edge_135)

    edge = np.sqrt(np.power(IconR1, 2.0) + np.power(IconR2, 2.0))
    edge = np.round(edge)
    edge[edge>255] = 255
    edge = edge.astype(np.uint8)

    cv2.imshow('edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()