import cv2 as cv  # pip install opencv-python
def getMask(rect1, rect2):
    (x1, y1, w1, h1) = rect1;       (x2, y2, w2, h2) = rect2
original_image = cv.imread('faces.jpg')
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
detected_faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, 
                                               minNeighbors=5)
for (x1, y1, width, height) in detected_faces:                                          
    rect = cv.rectangle(original_image, (x1, y1), (x1 + width, y1 + height), 
                        (0, 255, 0), 2 )

cv.imshow('Image', original_image)
cv.waitKey(0)
cv.destroyAllWindows()