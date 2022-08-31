from signal import signal
import numpy as np
import cv2
from scipy import signal

def prewitt(I, _boundary = 'symm'):
    # prewitt_x是可分離的，根據卷積運算結合律，分兩次小卷積核心運算
    # 垂直方向上的均值平滑
    ones_y = np.array([[1], [1], [1]], np.float32)
    i_conv_pre_x = signal.convolve2d(I, ones_y, mode = 'same', boundary = _boundary)
    # 水平方向上的差分
    diff_x = np.array([[1, 0, -1]], np.float32)
    i_conv_pre_x = signal.convolve2d(i_conv_pre_x, diff_x, mode = 'same', boundary = _boundary)

    # prewitt_y是可分離的，根據卷積運算結合律，分兩次小卷積核心運算
    # 水平方向上的均值平滑
    ones_x = np.array([[1, 1, 1]], np.float32)
    i_conv_pre_y = signal.convolve2d(I, ones_x, mode = 'same', boundary = _boundary)
    # 垂直方向上的差分
    diff_y = np.array([[1], [0], [-1]], np.float32)
    i_conv_pre_y = signal.convolve2d(i_conv_pre_y, diff_y, mode = 'same', boundary = _boundary)

    return (i_conv_pre_x, i_conv_pre_y)

if __name__ == '__main__':
    image = cv2.imread('../Image/img.jpg', cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', image)

    i_conv_pre_x, i_conv_pre_y = prewitt(image)
    
    abs_i_conv_pre_x = np.abs(i_conv_pre_x)
    abs_i_conv_pre_y = np.abs(i_conv_pre_y)

    edge_x = abs_i_conv_pre_x.copy()
    edge_y = abs_i_conv_pre_y.copy()

    edge_x[edge_x>255] = 255
    edge_y[edge_y>255] = 255

    cv2.imshow('edge_x', edge_x)
    cv2.imshow('edge_y', edge_y)

    edge = 0.5*abs_i_conv_pre_x + 0.5*abs_i_conv_pre_y
    edge[edge>255] = 255
    edge = edge.astype(np.uint8)

    cv2.imshow('edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()