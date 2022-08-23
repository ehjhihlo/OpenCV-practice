import numpy as np
from scipy import signal

if __name__ == "__main__":
    I = np.array([[1, 2], [3, 4]], np.float32)
    H1, W1 = I.shape[:2]
    # 卷積核心
    K = np.array([[-1, 2],[2, 1]], np.float32)
    H2, W2 = K.shape[:2]

    c_full = signal.convolve2d(I, K, mode = 'full')
    print(c_full)

    # 指定錨點位置
    kr, kc = 0, 0
    # 根據錨點位置，從full卷積中截取得到same卷積
    c_same = c_full[H2-kr-1:H1+H2-kr-1, W2-kc-1:W1+W2-kc-1]
    print(c_same)