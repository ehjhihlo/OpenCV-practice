import cv2
import numpy as np
import sys

def polar(I, center, r, theta=(0, 360), rstep=1.0, thetastep=360.0/(180*8)):
    # 得到距離和角度的最小、最大範圍
    minr, maxr = r
    mintheta, maxtheta = theta

    # 輸出圖像高、寬
    H = int((maxr - minr)/rstep) + 1
    W = int((maxtheta - mintheta)/thetastep) + 1
    O = 125*np.ones((H, W), I.dtype)
    # 極座標轉換
    r = np.linspace(minr, maxr, H)
    r = np.tile(r, (W, 1))
    r = np.transpose(r)
    theta = np.linspace(mintheta, maxtheta, W)
    theta = np.tile(theta, (H, 1))
    x, y = cv2.polarToCart(r, theta, angleInDegrees=True)

    # 最近插值法
    for i in range(H):
        for j in range(W):
            px = int(round(x[i][j]) + cx)
            py = int(round(y[i][j] + cy))
            if((px>=0 and px<=w-1) and (py>=0 and py<=h-1)):
                O[i][j] = I[py][px]
        return O

if __name__ == "__main__":
    I = cv2.imread("./Image/img.jpg")
    h, w = I.shape[:2]
    # 極座標轉換中心
    cx, cy = 508, 503
    cv2.circle(I, (int(cx), int(cy)), 10, (255,0,0,0), 3)

    # 距離的最小、最大半徑
    O = polar(I, (cx, cy), (200, 550))
    # 旋轉
    O = cv2.flip(O, 0)

    cv2.imshow("I", I)
    cv2.imshow("O", O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()