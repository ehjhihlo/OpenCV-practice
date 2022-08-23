import cv2
import numpy as np

# 計算以(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)以(1,1)為中心的極座標轉換
x = np.array([[0, 1, 2], [0, 1, 2], [0, 1, 2]], np.float64) - 1
y = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]], np.float64) - 1
r, theta = cv2.cartToPolar(x, y, angleInDegrees=True)
print('r = ', r)
print('theta = ', theta)
print('=========================================================')

# 計算極座標(30,10),(31,10),(30,11),(31,11)的笛卡兒座標
angle = np.array([[30, 31], [30, 31]], np.float32)
r = np.array([[10, 10], [11, 11]], np.float32)
x, y = cv2.polarToCart(r, angle, angleInDegrees=True)

# 以(-12, 15)為轉換中心
x += -12
y += 15

print('x = ', x)
print('y = ', y)