import cv2
import numpy as np

if __name__ == "__main__":
    I = cv2.imread("../Image/IMG_4230.JPG")
    # 求最大最小值
    Imax = np.max(I)
    Imin = np.min(I)
    # 要輸出的最小灰度級和最大灰度級
    Omin, Omax = 0, 255

    # 計算a和b的值
    a = float(Omax - Omin)/(Imax - Imin)
    b = Omin - a * Imin
    # 線性變換
    O = a * I + b

    O = O.astype(np.uint8)
    
    cv2.imshow("I", I)
    cv2.imshow("O", O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()