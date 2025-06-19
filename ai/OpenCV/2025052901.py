<<<<<<< HEAD
import argparse
import cv2
image = cv2.imread("image.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
# cv2.imshow("image before convert", image)
corner = image[0:100, 0:100]
# cv2.imshow("cutted image", corner)
corner = (0,255,0)
image[0:100,0:100] = corner
# cv2.imshow("updated image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import numpy as np
green = (0,255,0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
canvas = np.zeros_like(image)

cv2.line(canvas, (0,0), (300, 200), green, 1)

cv2.rectangle(canvas, (10, 20), (60, 80), green)

red = (0,0,255)
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)

blue = (255,0,0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255,255,255)

for r in range(0, 175, 25) : 
    cv2.circle(image, (centerX, centerY), r, white)
    
cv2.imshow("image before convert", image)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
=======
import argparse
import cv2
image = cv2.imread("image.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
# cv2.imshow("image before convert", image)
corner = image[0:100, 0:100]
# cv2.imshow("cutted image", corner)
corner = (0,255,0)
image[0:100,0:100] = corner
# cv2.imshow("updated image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import numpy as np
green = (0,255,0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
canvas = np.zeros_like(image)

cv2.line(canvas, (0,0), (300, 200), green, 1)

cv2.rectangle(canvas, (10, 20), (60, 80), green)

red = (0,0,255)
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)

blue = (255,0,0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255,255,255)

for r in range(0, 175, 25) : 
    cv2.circle(image, (centerX, centerY), r, white)
    
cv2.imshow("image before convert", image)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
>>>>>>> origin
