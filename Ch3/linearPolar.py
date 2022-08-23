import cv2

if __name__ == "__main__":
    src = cv2.imread("./Image/IMG_4230.JPG")
    cv2.imshow("src", src)
    
    # 圖像極座標轉換
    dst = cv2.linearPolar(src, (508, 503), 550, cv2.INTER_LINEAR)
    cv2.imwrite('./Image/linearPolar.jpg', dst)

    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()