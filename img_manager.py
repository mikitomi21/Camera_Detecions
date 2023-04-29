from skimage.io import imread, imshow
import os

def load_data(dir):
    imgs = []
    for file in os.listdir(dir):
        path = dir+file
        imgs.append(imread(path))
    return imgs