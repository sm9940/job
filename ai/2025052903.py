import cv2
from imutils import translate
import numpy as np

image = cv2.imread("image.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
#cv2.imshow("Original", image)

shifted = translate(image, 25, 50)
#cv2.imshow("Shift Down & Right", shifted)

shifted = translate(image, -25, -50)
#cv2.imshow("Shift Up & Left", shifted)

(h,w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated by 45 degrees", rotated)

M = cv2.getRotationMatrix2D(center, -45, 0.5)
rotated = cv2.warpAffine(image, M, (w, h))
#cv2.imshow("Rotated by -45 degrees", rotated)
# 과제 : 회전시 이미지가 윈도우에 패킹(꼭 맞게)되도록 한다...
# 오늘 실습 예제의 기능들을 모두 imutils.py에 넣어 모듈화한다.
r = 150/ image.shape[1]
dim = (150, int(image.shape[0] *r))
resized = cv2.resize(image, dim, 
                     interpolation=cv2.INTER_AREA)
#cv2.imshow("Resized (Width)", resized)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 255: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

M = np.ones(image.shape, dtype="uint8")* 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
M = np.ones(image.shape, dtype="uint8")* 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)

cv2.waitKey(0)
cv2.destroyAllWindows()
