# import numpy as np
# import cv2

# image = cv2.imread("image.jpg")
# cv2.imshow("Original", image)
# rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
# zeros = np.zeros(image.shape[:2], dtype="uint8")
# cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
# cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
# cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image_dark.jpg")
cv2.imshow("Original", image)
chans = cv2.split(image)
colors = ("b", "g", "r")

for (chan, color) in zip(chans, colors) :
    hist = cv2.calcHist(chan, [0], None, [256], [0,256])
    plt.plot(hist)
    plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()