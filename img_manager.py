import skimage
from skimage.transform import resize
from skimage.io import imread
import numpy as np
import os

def load_data(dir):
    images = []
    labels = []
    for file in os.listdir(dir):
        path = dir+file
        img = imread(path)
        resized_img = skimage.transform.resize(img, (80,80))
        
        images.append(resized_img)

        #TODO Think about labels later
        if file[0] == 'T':
            labels.append(1)
        else:
            labels.append(0)
        
    return images, labels
