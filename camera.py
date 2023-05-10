import cv2
import tensorflow as tf
import numpy as np
from keras.utils import load_img, img_to_array

def draw_border(img, color, thickness=5):
    height, width = img.shape[:2]
    cv2.rectangle(img, (0, 0), (width, height), color, thickness)

def check_img(path):
    img = load_img(path, target_size=(200,200))

    X = img_to_array(img)
    X = np.expand_dims(X, axis = 0)
    images = np.vstack([X])
    label = model.predict(images)

    if label == 0:
            print("Not Human")
            return 0
    elif label == 1:
            print("Human")
            return 1
    return 0

model = tf.keras.models.load_model('model/face_reco.h5')

camera = cv2.VideoCapture(0)

i=0
GREEN = (0,255,0)
RED = (0,0,255)
while (True):
    result, img = camera.read()

    if result:
        path = "img/Current_Camera.png"
        cv2.imwrite(path, img)
        label = check_img(path)
        if label:  
            draw_border(img, GREEN, 20)
        else:
            draw_border(img, RED, 20)
             

    cv2.imshow('frame', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i+=1


camera.release()
cv2.destroyAllWindows()