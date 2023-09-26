import os
import cv2
import tensorflow as tf

def shuffle(imgs: tf.Tensor, labels:tf.Tensor) -> tuple[list:tf.Tensor, list:tf.Tensor]:
    idx = tf.range(tf.shape(labels)[0])
    shuffled_idx = tf.random.shuffle(idx)
    imgs_tmp = tf.gather(imgs, shuffled_idx)
    labels_tmp = tf.gather(labels, shuffled_idx)
    return imgs_tmp, labels_tmp

def load_data() -> tuple[tuple[tf.Tensor, tf.Tensor], tuple[tf.Tensor, tf.Tensor]]:
    main_paths = ['img/train/', 'img/validation/']
    size = (224,224)
    is_human = False
    i = 0
    for main_path in main_paths:
        imgs = []
        labels = []
        for dir in os.listdir(main_path):
            if dir[0] == 'T':
                is_human = True
            elif dir[0] == 'F':
                is_human = False
            path = main_path + dir + '/'

            for file in os.listdir(path):
                img = cv2.imread(path+file)
                img = cv2.resize(img, size)
                img = img.astype(dtype="float32") / 255.0
                imgs.append(img)
                labels.append(is_human)
                i+=1
                # print(i)
                if i % 1000 == 0 and i > 0:
                    print(f"Uploaded {i} photos")

        imgs, labels = tf.constant(imgs), tf.constant(labels)
        imgs, labels = shuffle(imgs, labels)

        yield (imgs, labels)