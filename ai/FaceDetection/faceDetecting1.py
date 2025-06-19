<<<<<<< HEAD
#import cv2 as cv
import cv2 as cv

def getMask(rect1, rect2):
    (x1, y1, w1, h1) = rect1
    (x2, y2, w2, h2) = rect2


    # Read image from your local file system
original_image = cv.imread('C:\\Users\\IoT academy 21\\Downloads\\face5.jpg')

# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
detected_faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)
print(len(detected_faces))
# Display the resulting frame
for (x, y, w, h) in detected_faces:
    cv.rectangle(original_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = grayscale_image[y:y + h, x:x + w]
    roi_color = original_image[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.05, minNeighbors=7)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv.imshow('Image', original_image)
cv.waitKey(0)
=======
#import cv2 as cv
import cv2 as cv

def getMask(rect1, rect2):
    (x1, y1, w1, h1) = rect1
    (x2, y2, w2, h2) = rect2


    # Read image from your local file system
original_image = cv.imread('C:\\Users\\IoT academy 21\\Downloads\\face5.jpg')

# Convert color image to grayscale for Viola-Jones
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
detected_faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)
print(len(detected_faces))
# Display the resulting frame
for (x, y, w, h) in detected_faces:
    cv.rectangle(original_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = grayscale_image[y:y + h, x:x + w]
    roi_color = original_image[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.05, minNeighbors=7)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

cv.imshow('Image', original_image)
cv.waitKey(0)
>>>>>>> origin
cv.destroyAllWindows()