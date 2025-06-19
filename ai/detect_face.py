<<<<<<< HEAD
import numpy as np; from PIL import Image; import cv2
def detect_face(img):
    mt_res = detector.detect_faces(img)
    return_res = []
    for face in mt_res:
        x, y, width, height = face['box']
        center = [x+(width/2), y+(height/2)]
        max_border = max(width, height)
        # center alignment
        left = max(int(center[0]-(max_border/2)), 0)
        right = max(int(center[0]+(max_border/2)), 0)
        top = max(int(center[1]-(max_border/2)), 0)
        bottom = max(int(center[1]+(max_border/2)), 0)
        # crop the face
        center_img_k = img[top:top+max_border, left:left+max_border, :]
        center_img = np.array(Image.fromarray(center_img_k).resize([256, 256]))
        # create predictions
        age_preds = age_model.predict(np.expand_dims(center_img/255, 0), verbose=0)
        max_age_preds = np.array(max(age_preds[0]))
        idx_max_age_preds = np.where(age_preds == max_age_preds)[1][0]
        gender_preds = gender_model.predict(np.expand_dims(center_img/255, 0),
                                            verbose=0)[0][0]
        # output to the cv2
        return_res.append([top, right, bottom, left, gender_preds,
                            max_age_preds, idx_max_age_preds])

=======
import numpy as np; from PIL import Image; import cv2
def detect_face(img):
    mt_res = detector.detect_faces(img)
    return_res = []
    for face in mt_res:
        x, y, width, height = face['box']
        center = [x+(width/2), y+(height/2)]
        max_border = max(width, height)
        # center alignment
        left = max(int(center[0]-(max_border/2)), 0)
        right = max(int(center[0]+(max_border/2)), 0)
        top = max(int(center[1]-(max_border/2)), 0)
        bottom = max(int(center[1]+(max_border/2)), 0)
        # crop the face
        center_img_k = img[top:top+max_border, left:left+max_border, :]
        center_img = np.array(Image.fromarray(center_img_k).resize([256, 256]))
        # create predictions
        age_preds = age_model.predict(np.expand_dims(center_img/255, 0), verbose=0)
        max_age_preds = np.array(max(age_preds[0]))
        idx_max_age_preds = np.where(age_preds == max_age_preds)[1][0]
        gender_preds = gender_model.predict(np.expand_dims(center_img/255, 0),
                                            verbose=0)[0][0]
        # output to the cv2
        return_res.append([top, right, bottom, left, gender_preds,
                            max_age_preds, idx_max_age_preds])

>>>>>>> origin
    return return_res