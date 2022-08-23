import cv2

if __name__ == "__main__":
    src = cv2.imread("../Image/IMG_4230.JPG", cv2.IMREAD_ANYCOLOR)
    dst = cv2.normalize(src, 255, 0, cv2.NORM_MINMAX, cv2.CV_8U)
    
    cv2.imshow("src", src)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()