import cv2

if __name__ == "__main__":
    src = cv2.imread("./Image/IMG_4230.JPG")
    cv2.imshow("src", src)
    
    # 圖像極座標轉換
    M = 50
    dst = cv2.logPolar(src, (508, 503), M, cv2.WARP_FILL_OUTLIERS)
    cv2.imwrite('./Image/logPolar_M50.jpg', dst)

    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()