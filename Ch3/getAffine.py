import cv2
import numpy as np

src = np.array([[0, 0],[200, 0],[0, 200]], np.float32)
dst = np.array([[0, 0],[100, 0],[0, 100]], np.float32)
A = cv2.getAffineTransform(src, dst)
print(A)