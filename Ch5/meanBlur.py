from pickletools import uint8
import cv2
import numpy as np

def integral(image):
    rows, cols = image.shape
    # 行積分運算
    inteImageC = np.zeros((rows, cols), np.float32)
    for row in range(rows):
        for col in range(cols):
            if col == 0:
                inteImageC[row][col] = image[row][col]
            else:
                inteImageC[row][col] = inteImageC[row][col-1] + image[row][col]
    # 列積分運算
    inteImage = np.zeros(image.shape, np.float32)
    for col in range(cols):
        for row in range(rows):
            if row == 0:
                inteImage[row][col] = inteImageC[row][col]
            else:
                inteImage[row][col] = inteImage[row][col-1] + inteImageC[row][col]
    # 上邊和左邊補0
    inteImage_0 = np.zeros((rows+1, cols+1), np.float32)
    inteImage_0[1:rows+1, 1:cols+1] = inteImage

    return inteImage_0   

def fastMeanBlur(image, winSize, bordertype = cv2.BORDER_DEFAULT):
    halfW = int((winSize[0]-1)/2)
    halfH = int((winSize[1]-1)/2)
    ratio = 1.0/(winSize[0]*winSize[1])

    # 圖像高寬
    rows, cols = image.shape
    # 邊界擴充
    paddImage = np.zeros((rows+1, cols+1), np.float32)
    paddImage[1:rows+1, 1:cols+1] = image
    # paddImage = cv2.copyMakeBorder(image, halfH, halfH, halfW, halfW, bordertype)
    # paddImage = image
    # 圖像積分
    paddIntegral = integral(paddImage)

    # 均值濾波後的結果
    meanBlurImage = np.zeros(image.shape, np.float32)
    r, c = 0, 0
    for h in range(halfH, halfH + rows, 1):
        for w in range(halfW, halfW + cols, 1):
            meanBlurImage[r][c] = (paddIntegral[h+halfH+1][w+halfW+1]+paddIntegral[h-halfH][w-halfW]
            -paddIntegral[h+halfH+1][w-halfW]-paddIntegral[h-halfH][w+halfW+1]) * ratio
            c += 1
        r += 1
        c = 0
    
    return meanBlurImage

if __name__ == '__main__':
    image = cv2.imread('../Image/img.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 均值平滑
    meanBlurImage = fastMeanBlur(image, (7, 7), bordertype = cv2.BORDER_DEFAULT)
    # 對blurImage進行灰度級顯示
    meanBlurImage = np.round(meanBlurImage)
    meanBlurImage = meanBlurImage.astype(uint8)
    cv2.imshow('image', image)
    cv2.imshow('MeanBlur', meanBlurImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()