import cv2
import numpy as np

if __name__ == "__main__":
    src = cv2.imread("../Image/img.jpg", cv2.IMREAD_ANYCOLOR)
    # 創建clahe對象
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    
    dst = clahe.apply(src)
    
    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()