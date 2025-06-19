<<<<<<< HEAD
import numpy as np
import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
mask = np.zeros(image.shape[:2], dtype="uint8")
print(mask.shape)
cv2.rectangle(mask, (25,25), (275, 275), 255, -1)
# cv2.imshow("Mask", mask)

bitwiseAnd = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("And", bitwiseAnd)

cv2.waitKey(0)
=======
import numpy as np
import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
mask = np.zeros(image.shape[:2], dtype="uint8")
print(mask.shape)
cv2.rectangle(mask, (25,25), (275, 275), 255, -1)
# cv2.imshow("Mask", mask)

bitwiseAnd = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("And", bitwiseAnd)

cv2.waitKey(0)
>>>>>>> origin
cv2.destroyAllWindows()