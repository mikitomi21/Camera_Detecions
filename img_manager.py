from skimage import transform
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import os

X_SIZE = 26
Y_SIZE = 26

def load_data(dir):
    images = []
    labels = []
    for file in os.listdir(dir):
        path = dir+file
        img = imread(path)

        # Change a size
        img = transform.resize(img, (Y_SIZE, X_SIZE))

        # Change a color
        img = rgb2gray(img)

        images.append(img)

        #TODO Think about labels later
        if file[0] == 'T':
            labels.append(1)
        else:
            labels.append(0)
        
    return images, labels
