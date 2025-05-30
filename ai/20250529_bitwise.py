import numpy as np
import cv2


image = cv2.imread('C:/Users/Administrator/Desktop/himedia/job/ai/image.jpg')
cv2.imshow("Original",image)
mask = np.zeros(image.shape[:2],dtype="uint8")

rectangle = np.zeros((300,300), dtype='uint8')
cv2.rectangle(mask, (25,25), image, 255, -1)
cv2.imshow('Rectangle', rectangle)

circle = np.zeros((300,300), dtype='uint8')
cv2.circle(image, (150,150), 150, 255, -1)
cv2.imshow('Circle', circle)


# bitwiseAnd = cv2.bitwise_and(rectangle, circle)
# cv2.imshow('AND', bitwiseAnd)

# bitwiseOr = cv2.bitwise_or(rectangle, circle)
# cv2.imshow('OR', bitwiseOr)

# bitwseXor = cv2.bitwise_xor(rectangle, circle)
# cv2.imshow('XOR', bitwseXor)

# bitwiseNot = cv2.bitwise_not(circle)
# cv2.imshow('NOT', bitwiseNot)


bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow('AND', bitwiseAnd)



cv2.waitKey(0)
cv2.destroyAllWindows()