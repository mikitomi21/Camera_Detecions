from skimage.io import imread, imshow
import os

def load_data(dir):
    images = []
    labels = []
    for file in os.listdir(dir):
        path = dir+file
        images.append(imread(path))

        #TODO Think about labels later
        labels.append(1)
    return images, labels