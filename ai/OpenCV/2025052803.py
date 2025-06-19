<<<<<<< HEAD
import argparse
import cv2
image = cv2.imread("image.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))
cv2.imshow("image before convert", image)
(b,g,r) = image[97,366]
print("Pixel at (366,97): Red : {}, Green : {}, Blue : {}".format(r,g,b))
image[97,366] = (255,0,0)
(b,g,r) = image[97,366]
print("Pixel at (366,97): Red : {}, Green : {}, Blue : {}".format(r,g,b))
cv2.imshow("image after convert", image)
cv2.waitKey(0)
=======
import argparse
import cv2
image = cv2.imread("image.jpg")
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))
cv2.imshow("image before convert", image)
(b,g,r) = image[97,366]
print("Pixel at (366,97): Red : {}, Green : {}, Blue : {}".format(r,g,b))
image[97,366] = (255,0,0)
(b,g,r) = image[97,366]
print("Pixel at (366,97): Red : {}, Green : {}, Blue : {}".format(r,g,b))
cv2.imshow("image after convert", image)
cv2.waitKey(0)
>>>>>>> origin
cv2.destroyAllWindows()