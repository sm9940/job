import cv2
import numpy as np
from PIL import Image 

def detect_face(img):
    mt_res = detector.detect_faces(img)
    return_res=[]
    for face in mt_res:
        x,y,width, height =face['box']
        center = [x+(width/2),y+(height/2)]
        max_border = max(width,height)

        left =max(int(center[0]-(max_border/2)),0)
        right = max(int(center[0]+(max_border/2)),0)
        top =max(int(center[1]-(max_border/2)),0)
        bottom = max(int(center[1]+(max_border/2)),0)

        center_img_k = img[top:top+max_border,left:left+max_border,:]
        center_img = np.array(Image.fromarray(center_img_k).resize([256,256,]))

        age_preds = age.model.predict(np.expand_dims(center_img/255,0),verbose=0)
        max_age_preds = np.array(max(age_preds[0]))
        idx_max_age_preds =np.where(age_preds=max_age_preds)[1][0]
        gender_preds = gender_model.predict(np.expand_dims(center_img/255,0),verbose=0)[0][0]

        return_res.append([top,right,bottom,left,gender_preds,max_age_preds,idx_max_age_preds])

    return return_res