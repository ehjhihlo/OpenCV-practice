import cv2
import numpy as np

if __name__ == "__main__":
    I = cv2.imread("../Image/IMG_4230.JPG", cv2.IMREAD_ANYCOLOR)
    fI = I/255.0
    
    # Gamma轉換
    gamma = 0.5 # 0 < gamma < 1調亮 / gamma > 1調暗
    O = np.power(fI, gamma)
    
    cv2.imshow("I", I)
    cv2.imshow("O", O)
    cv2.waitKey(0)
    cv2.destroyAllWindows()