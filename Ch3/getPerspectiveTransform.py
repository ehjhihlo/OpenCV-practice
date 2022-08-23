import cv2
import numpy as np

src = np.array([[0, 0],[200, 0],[0, 200],[200, 200]], np.float32)
dst = np.array([[100, 20],[200, 20],[50, 70],[250, 70]], np.float32)
A = cv2.getPerspectiveTransform(src, dst)
print(A)

if __name__ == '__main__':
    image = cv2.imread('./img.jpg')
    h, w = image.shape[:2]
    src = np.array([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]], np.float32)
    dst = np.array([[50, 50], [w/3, 50], [50, h-1], [w-1, h-1]], np.float32)

    p = cv2.getPerspectiveTransform(src, dst)
    r = cv2.warpPerspective(image, p, (w,h), borderValue = 125)
    cv2.imshow("image", image)
    cv2.imshow("wrapPerspective", r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()