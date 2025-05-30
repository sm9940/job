import cv2 
def getMask(rect1,rect2):
    (x1,y1,w1,h1) = rect1
    (x2, y2, w2, h2) = rect2
video_capture = cv2.VideoCapture(0)
while True :
    ret,frame = video_capture.read()
    rgb_frame = frame[:,:,::-1]

    original_image = frame
    grayscale_image = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('C:/Users/Administrator/Desktop/himedia/job/ai/haarcascade_frontalface_default.xml')
    detected_faces = face_cascade.detectMultiScale(grayscale_image,scaleFactor=1.1, minNeighbors=5)

    for(x1,y1,width,height) in detected_faces :
        rect =  cv2.rectangle(original_image,(x1,y1),(x1+width,y1 + height),(0,0,255),2)
    
    cv2.imshow("Video",frame)
    if cv2.waitKey(5)==27:
        break
video_capture.release()
cv2.destroyAllWindows()
