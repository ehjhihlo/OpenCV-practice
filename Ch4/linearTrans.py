import cv2
import numpy as np

if __name__ == "__main__":
    I = cv2.imread("../Image/IMG_4230.JPG")

    # 線性變換
    a = 2
    O = float(a)*I
    # 大於255的要截斷為255
    O[O > 255] = 255
    O = np.round(O)
    O = O.astype(np.uint8)

    cv2.imshow("I", I)
    cv2.imshow("O", O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()