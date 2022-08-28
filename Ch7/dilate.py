import cv2

if __name__ == "__main__":
    I = cv2.imread("../Image/img.jpg", cv2.COLOR_BGR2GRAY)
    cv2.imshow('I', I)
    # 結構半徑
    r = 1
    MAX_R = 20
    cv2.namedWindow('dilate', 1)

    def nothing(*arg):
        pass
    # 調節結構元半徑
    cv2.createTrackbar('r', 'dilate', r, MAX_R, nothing)
    while True:
        # 得到當前r值
        r = cv2.getTrackbarPos('r', 'dilate')
        # 創建結構元
        s = cv2.getStructuringElement(cv2.MORPH_RECT, (2*r+1, 2*r+1))
        # 膨脹圖像
        d = cv2.dilate(I, s)
        # 顯示膨脹效果
        cv2.imshow('dilate', d)
        ch = cv2.waitKey(5)
        if ch == 27:
            break
        cv2.destroyAllWindows()