import tensorflow as tf
import matplotlib.pyplot as plt
import os
from pathlib import Path
from skimage.io import imread, imshow
from skimage import data

def load_data(data_path):
    labels = []
    images = []
    for file in os.listdir(data_path):

        images.append(data.imread(os.path.join(data_path, file)))
        labels.append(file)
    return images, labels

# image_gray = imread('img/Test_photo0.png', as_gray=True)
# imshow(image_gray)
image_gray = imread('Test_photo56.png')
imshow(image_gray)
plt.imshow(image_gray)

# ROOT_PATH = "img/"
#
# images, labels = load_data(ROOT_PATH)
#
# for i in range(4):
#     plt.subplot(1,4,i+1)
#     plt.axis('off')
#     plt.imshow(images[i])
#     plt.show()