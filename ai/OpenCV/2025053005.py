import numpy as np
import cv2

image = cv2.imread("coin.jpg")
cv2.imshow("Original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)
cv2.imwrite("grayImage.jpg", gray)
# blurred = cv2.GaussianBlur(gray, (5,5), 0)
# blurred = cv2.blur(gray, (7,7))
blurred = cv2.blur(gray, (5,5))
# blurred = cv2.blur(blurred, (5,5))
cv2.imshow("Gaussian", blurred)

# (T, thresh) = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
# thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
# cv2.imshow("Mean Threshold", thresh)
# # 과제 1 : 침식/팽창 -> 열림/닫힘 연산 : 내/외부 노이즈를 제거할 수 있다.
#
# # (T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
# thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
# cv2.imshow("Gaussian Threshold", thresh)

import mahotas
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold:{}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

T = mahotas.thresholding.rc(blurred)
print("RC's threshold:{}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()