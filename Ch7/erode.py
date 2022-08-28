import cv2

if __name__ == "__main__":
    I = cv2.imread("../Image/img.jpg", cv2.COLOR_BGR2GRAY)
    # 創建矩形結構元
    s = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 腐蝕圖像，迭代數採用預設值1
    r = cv2.erode(I, s)
    # 邊界提取
    e = I - r

    cv2.imshow('I', I)
    cv2.imshow('erode', r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()