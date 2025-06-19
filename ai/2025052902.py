<<<<<<< HEAD
import cv2
import detect_face
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    # face_locations = detect_face(rgb_frame)
    # for top, right, bottom, left, gender_preds, max_age_preds, \
    #     idx_max_age_preds in face_locations:
    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(5) == 27 :
        break
video_capture.release()
=======
import cv2
import detect_face
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    rgb_frame = frame[:, :, ::-1]
    # face_locations = detect_face(rgb_frame)
    # for top, right, bottom, left, gender_preds, max_age_preds, \
    #     idx_max_age_preds in face_locations:
    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.imshow('Video', frame)
    if cv2.waitKey(5) == 27 :
        break
video_capture.release()
>>>>>>> origin
cv2.destroyAllWindows()