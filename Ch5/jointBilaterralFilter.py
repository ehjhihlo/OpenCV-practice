import cv2
import numpy as np
import math

def getClosenessWeight(sigma_g, H, W):
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H-1)/2
    c -= (W-1)/2
    closeWeight = np.exp(-0.5*(np.power(r, 2)) + np.power(c, 2)) / math.pow(sigma_g, 2)
    return closeWeight

def jointBLF(I, H, W, sigma_g, sigma_d, borderType=cv2.BORDER_DEFAULT):
    clossenWeight = getClosenessWeight(sigma_g, H, W)
    
    Ig = cv2.GaussianBlur(I, (W, H), sigma_g)
    
    cH = (H-1)/2
    cW = (W-1)/2

    Ip = cv2.copyMakeBorder(I, cH, cH, cW, cW, borderType)
    Igp = cv2.copyMakeBorder(Ig, cH, cH, cW, cW, borderType)

    rows, cols = I.shape
    i, j = 0, 0

    jblf = np.zeros(I.shape, np.float64)

    for r in np.arange(cH, cH+cols, 1):
        for c in np.arange(cW, cW+rows, 1):
            pixel = Igp[r][c]
            rTop, rBottom = r-cH, r+cH
            cLeft, cRight = c-cW, c+cW

            region = Igp[rTop:rBottom+1][cLeft:cRight+1]
            similarityWeight = np.exp(-0.5*np.power(region-pixel, 2.0)/math.pow(sigma_d, 2.0))
            weight = clossenWeight*similarityWeight
            weight = weight/np.sum(weight)

            jblf[i][j] = np.sum(Ip[rTop:rBottom+1, cLeft:cRight+1] * weight)
            j += 1
        j = 0
        i += 1
    
    return jblf

if __name__ == '__main__':
    I = cv2.imread('../Image/img.jpg')
    I = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
    fI = I.astype(np.float64)
    jblf = jointBLF(fI, 33, 33, 7, 2)
    jblf = jblf.astype(np.uint8)
    cv2.imshow('jblf', jblf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()