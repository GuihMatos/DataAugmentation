import cv2
import os
import tensorflow as tf

folder = "/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/IN_LOCO/output4/train/class_1/"

i = 0
for filename in os.listdir(folder):
    image = folder + filename
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = tf.image.rot90(image)
    image180 = tf.image.rot90(image)
    hor_180_image = tf.image.flip_left_right(image180)

    new_name = "hor_180_" + filename
    
    tf.keras.preprocessing.image.save_img(f"/home/guilherme/PIXFORCE/REDSOFT/MARFRIG/IN_LOCO/output4/train/aug1/{new_name}", hor_180_image)
    i+=1
    print(i)