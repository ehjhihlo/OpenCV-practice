# 開運算：先腐蝕後膨脹
# 閉運算：先膨脹後腐蝕
# 頂帽轉換：影像減去開運算結果
# 底帽轉換：影像減去閉運算結果
# 形態學梯度：開運算 - 閉運算


import cv2

if __name__ == "__main__":
    I = cv2.imread("../Image/img.jpg", cv2.COLOR_BGR2GRAY)
    cv2.imshow("I", I)
    # 結構半徑，迭代次數
    r, i = 1, 1
    MAX_R, MAX_I = 20, 20
    # 顯示形態學處理效果的窗口
    cv2.namedWindow('morphology', 1)

    def nothing(*arg):
        pass

    # 調節結構元半徑
    cv2.createTrackbar('r', 'morphology', r, MAX_R, nothing)
    # 調節迭代次數
    cv2.createTrackbar('i', 'morphology', i, MAX_I, nothing)

    while True:
        # 得到當前r, i值
        r = cv2.getTrackbarPos('r', 'morphology')
        i = cv2.getTrackbarPos('i', 'morphology')
        # 創建結構元
        s = cv2.getStructuringElement(cv2.MORPH_RECT, (2*r+1, 2*r+1))
        # 形態學處理
        d = cv2.morphologyEx(I, cv2.MORPH_OPEN, s, iterations=i)
        # 顯示膨脹效果
        cv2.imshow('morphology', d)
        ch = cv2.waitKey(5)
        if ch == 27:
            break
        cv2.destroyAllWindows()